#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memory Guardian - Cleanup Script
内存守护者 - 清理脚本

Cross-platform Python/Node.js process cleanup for AI development environments.
跨平台 Python/Node.js 进程清理，适用于 AI 开发环境。

Author: Agents-MD Pro
License: MIT
"""

import os
import sys
import signal
from pathlib import Path
from datetime import datetime

try:
    import psutil
except ImportError:
    print("Error: psutil not installed. Run: pip install psutil")
    print("错误：未安装 psutil。请运行：pip install psutil")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install PyYAML")
    print("错误：未安装 PyYAML。请运行：pip install PyYAML")
    sys.exit(1)


class ProcessCleaner:
    """Safe process cleanup for Python and Node.js."""
    
    def __init__(self, config_path: str = None):
        """Initialize the Process Cleaner."""
        self.script_dir = Path(__file__).parent.parent
        self.config_path = config_path or self.script_dir / "config.yaml"
        self.config = self._load_config()
        self.current_pid = os.getpid()
        self.current_ppid = os.getppid()
        
    def _load_config(self) -> dict:
        """Load configuration from YAML file."""
        default_config = {
            "target_processes": ["python", "python3", "python.exe", "pythonw.exe", "node", "node.exe"],
        }
        
        try:
            if Path(self.config_path).exists():
                with open(self.config_path, "r", encoding="utf-8") as f:
                    loaded = yaml.safe_load(f)
                    if loaded:
                        default_config.update(loaded)
        except Exception as e:
            print(f"Warning: Could not load config: {e}")
            
        return default_config
    
    def get_target_processes(self) -> list:
        """Get list of Python/Node.js processes with their info."""
        target_names = [name.lower() for name in self.config.get("target_processes", [])]
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'status', 'create_time', 'cmdline']):
            try:
                pinfo = proc.info
                pname = pinfo['name'].lower() if pinfo['name'] else ''
                
                # Skip if not a target process
                if not any(target in pname for target in target_names):
                    continue
                
                # Skip current process and its parent
                if pinfo['pid'] in [self.current_pid, self.current_ppid]:
                    continue
                
                # Get memory in MB
                memory_mb = pinfo['memory_info'].rss / (1024 * 1024) if pinfo['memory_info'] else 0
                
                # Get command line (truncated)
                cmdline = " ".join(pinfo['cmdline'][:3]) if pinfo['cmdline'] else "N/A"
                if len(cmdline) > 60:
                    cmdline = cmdline[:57] + "..."
                
                # Determine process type
                if "python" in pname:
                    proc_type = "Python"
                elif "node" in pname:
                    proc_type = "Node.js"
                else:
                    proc_type = "Other"
                
                processes.append({
                    "pid": pinfo['pid'],
                    "name": pinfo['name'],
                    "type": proc_type,
                    "memory_mb": memory_mb,
                    "status": pinfo['status'],
                    "cmdline": cmdline
                })
                
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        # Sort by memory usage (descending)
        processes.sort(key=lambda x: x['memory_mb'], reverse=True)
        return processes
    
    def display_processes(self, processes: list):
        """Display processes in a formatted table."""
        if not processes:
            print("\n没有发现可清理的 Python/Node.js 进程。")
            print("No cleanable Python/Node.js processes found.\n")
            return
        
        print("\n" + "=" * 80)
        print("📋 可清理的进程列表 / Cleanable Processes")
        print("=" * 80)
        print()
        
        # Table header
        print(f"{'ID':<4} {'类型/Type':<10} {'PID':<8} {'内存/Memory':<12} {'状态/Status':<10} {'命令/Command'}")
        print("-" * 80)
        
        for i, proc in enumerate(processes, 1):
            status = proc['status'][:8] if len(proc['status']) > 8 else proc['status']
            print(f"{i:<4} {proc['type']:<10} {proc['pid']:<8} {proc['memory_mb']:.1f} MB{'':<4} {status:<10} {proc['cmdline'][:40]}")
        
        print("-" * 80)
        
        # Calculate total
        total_mb = sum(p['memory_mb'] for p in processes)
        print(f"{'总计/Total:':<24} {total_mb:.1f} MB ({len(processes)} 个进程/processes)")
        print()
    
    def terminate_process(self, pid: int) -> bool:
        """Safely terminate a process."""
        try:
            proc = psutil.Process(pid)
            proc_name = proc.name()
            
            # First try graceful termination
            proc.terminate()
            
            # Wait for termination (max 5 seconds)
            try:
                proc.wait(timeout=5)
                return True
            except psutil.TimeoutExpired:
                # Force kill if graceful termination failed
                proc.kill()
                proc.wait(timeout=3)
                return True
                
        except psutil.NoSuchProcess:
            print(f"  进程 {pid} 已经终止 / Process {pid} already terminated")
            return True
        except psutil.AccessDenied:
            print(f"  ❌ 无权限终止进程 {pid} / Access denied for process {pid}")
            return False
        except Exception as e:
            print(f"  ❌ 终止进程 {pid} 失败: {e} / Failed to terminate {pid}: {e}")
            return False
    
    def cleanup_interactive(self):
        """Interactive cleanup with user confirmation."""
        processes = self.get_target_processes()
        
        if not processes:
            print("\n✅ 没有发现可清理的 Python/Node.js 进程。")
            print("   No cleanable Python/Node.js processes found.\n")
            return
        
        self.display_processes(processes)
        
        print("请选择要终止的进程 / Select processes to terminate:")
        print("  - 输入进程编号，用逗号分隔 / Enter IDs, comma-separated (e.g., 1,3,5)")
        print("  - 输入 'all' 清理全部 / Enter 'all' to clean all")
        print("  - 输入 'q' 取消 / Enter 'q' to cancel")
        print()
        
        try:
            response = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n已取消 / Cancelled\n")
            return
        
        if response in ['q', 'quit', 'exit', '取消']:
            print("\n已取消 / Cancelled\n")
            return
        
        # Determine which processes to terminate
        to_terminate = []
        
        if response == 'all':
            to_terminate = processes
        else:
            try:
                ids = [int(x.strip()) for x in response.split(',') if x.strip()]
                for idx in ids:
                    if 1 <= idx <= len(processes):
                        to_terminate.append(processes[idx - 1])
                    else:
                        print(f"  ⚠️ 无效的编号: {idx} / Invalid ID: {idx}")
            except ValueError:
                print("  ❌ 输入格式错误 / Invalid input format")
                return
        
        if not to_terminate:
            print("\n没有选择任何进程 / No processes selected\n")
            return
        
        # Confirm before termination
        total_mb = sum(p['memory_mb'] for p in to_terminate)
        print()
        print(f"⚠️ 即将终止 {len(to_terminate)} 个进程，释放约 {total_mb:.1f} MB 内存")
        print(f"   About to terminate {len(to_terminate)} processes, freeing ~{total_mb:.1f} MB")
        print()
        print("确认终止？ / Confirm termination? (Y/N)")
        
        try:
            confirm = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n已取消 / Cancelled\n")
            return
        
        if confirm not in ['y', 'yes', '是', '确认']:
            print("\n已取消 / Cancelled\n")
            return
        
        # Terminate processes
        print()
        print("正在终止进程 / Terminating processes...")
        print()
        
        success_count = 0
        freed_mb = 0
        
        for proc in to_terminate:
            print(f"  终止 / Terminating: {proc['type']} (PID {proc['pid']}) - {proc['memory_mb']:.1f} MB")
            if self.terminate_process(proc['pid']):
                success_count += 1
                freed_mb += proc['memory_mb']
                print(f"    ✅ 成功 / Success")
        
        print()
        print("=" * 60)
        print(f"✅ 清理完成 / Cleanup Complete")
        print(f"   成功终止 / Successfully terminated: {success_count}/{len(to_terminate)} 个进程/processes")
        print(f"   释放内存 / Memory freed: ~{freed_mb:.1f} MB")
        print("=" * 60)
        print()
        
        # Show new memory status
        import time
        time.sleep(1)  # Wait for memory to be released
        
        mem = psutil.virtual_memory()
        print(f"🔄 当前内存状态 / Current Memory Status:")
        print(f"   使用率 / Usage: {mem.percent:.1f}%")
        print(f"   可用 / Available: {mem.available / (1024**3):.1f} GB")
        print()


def main():
    """Main entry point."""
    print()
    print("=" * 60)
    print("🧹 Memory Guardian - 进程清理 / Process Cleanup")
    print("=" * 60)
    print()
    print("此工具将帮助您安全地清理 Python/Node.js 进程。")
    print("This tool helps you safely clean up Python/Node.js processes.")
    print()
    print("⚠️ 注意：当前进程和父进程将被保护，不会被清理。")
    print("   Note: Current process and parent process are protected.")
    print()
    
    cleaner = ProcessCleaner()
    cleaner.cleanup_interactive()


if __name__ == "__main__":
    main()
