#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memory Guardian - Monitor Script
内存守护者 - 监控脚本

Cross-platform memory monitoring for AI development environments.
跨平台内存监控，适用于 AI 开发环境。

Author: Agents-MD Pro
License: MIT
"""

import os
import sys
import time
import argparse
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

# Try to import plyer for notifications (optional)
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False


class MemoryGuardian:
    """Memory monitoring and alerting system."""
    
    def __init__(self, config_path: str = None):
        """Initialize the Memory Guardian."""
        self.script_dir = Path(__file__).parent.parent
        self.config_path = config_path or self.script_dir / "config.yaml"
        self.config = self._load_config()
        self.last_notification_time = 0
        
    def _load_config(self) -> dict:
        """Load configuration from YAML file."""
        default_config = {
            "thresholds": {"notice": 70, "warning": 80, "critical": 90},
            "check_interval": 30,
            "notification_cooldown": 60,
            "target_processes": ["python", "python3", "python.exe", "pythonw.exe", "node", "node.exe"],
            "enable_notifications": True,
            "enable_console": True,
            "language": "bilingual"
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
    
    def get_memory_usage(self) -> tuple:
        """Get physical memory usage percentage and available memory in GB."""
        mem = psutil.virtual_memory()
        used_percent = mem.percent
        available_gb = mem.available / (1024 ** 3)
        total_gb = mem.total / (1024 ** 3)
        used_gb = mem.used / (1024 ** 3)
        return used_percent, available_gb, total_gb, used_gb
    
    def get_level(self, usage: float) -> str:
        """Determine the alert level based on memory usage."""
        thresholds = self.config["thresholds"]
        if usage >= thresholds["critical"]:
            return "critical"
        elif usage >= thresholds["warning"]:
            return "warning"
        elif usage >= thresholds["notice"]:
            return "notice"
        return "normal"
    
    def get_level_icon(self, level: str) -> str:
        """Get icon for the alert level."""
        icons = {
            "normal": "🟢",
            "notice": "🟡",
            "warning": "🟠",
            "critical": "🔴"
        }
        return icons.get(level, "⚪")
    
    def format_message(self, level: str, usage: float, available_gb: float) -> tuple:
        """Format alert message in bilingual format."""
        lang = self.config.get("language", "bilingual")
        icon = self.get_level_icon(level)
        
        messages = {
            "normal": {
                "title_zh": "内存状态正常",
                "title_en": "Memory Status Normal",
                "body_zh": f"当前物理内存使用率: {usage:.1f}%\n可用内存: {available_gb:.1f} GB",
                "body_en": f"Current physical memory usage: {usage:.1f}%\nAvailable: {available_gb:.1f} GB"
            },
            "notice": {
                "title_zh": "💡 内存提醒",
                "title_en": "💡 Memory Notice",
                "body_zh": f"当前物理内存使用率: {usage:.1f}%\n可用内存: {available_gb:.1f} GB\n\n建议关注内存情况。",
                "body_en": f"Current physical memory usage: {usage:.1f}%\nAvailable: {available_gb:.1f} GB\n\nConsider monitoring memory usage."
            },
            "warning": {
                "title_zh": "⚠️ 内存警告",
                "title_en": "⚠️ Memory Warning",
                "body_zh": f"当前物理内存使用率: {usage:.1f}%\n可用内存: {available_gb:.1f} GB\n\n建议暂停当前任务，避免被迫中断！",
                "body_en": f"Current physical memory usage: {usage:.1f}%\nAvailable: {available_gb:.1f} GB\n\nConsider pausing your task to avoid forced interruption!"
            },
            "critical": {
                "title_zh": "🚨 严重警告！",
                "title_en": "🚨 CRITICAL WARNING!",
                "body_zh": f"当前物理内存使用率: {usage:.1f}%\n可用内存: {available_gb:.1f} GB\n\n⚠️ 内存即将耗尽！系统可能随时崩溃！\n强烈建议立即暂停工作并清理内存！",
                "body_en": f"Current physical memory usage: {usage:.1f}%\nAvailable: {available_gb:.1f} GB\n\n⚠️ Memory almost exhausted! System may crash!\nSTRONGLY recommend pausing work and cleaning memory NOW!"
            }
        }
        
        msg = messages.get(level, messages["normal"])
        
        if lang == "zh":
            return msg["title_zh"], msg["body_zh"]
        elif lang == "en":
            return msg["title_en"], msg["body_en"]
        else:  # bilingual
            title = f"{msg['title_zh']} / {msg['title_en']}"
            body = f"{msg['body_zh']}\n\n{'─' * 40}\n\n{msg['body_en']}"
            return title, body
    
    def send_notification(self, title: str, message: str, level: str):
        """Send desktop notification if available."""
        if not self.config.get("enable_notifications", True):
            return
            
        if not PLYER_AVAILABLE:
            return
            
        # Check cooldown
        current_time = time.time()
        cooldown = self.config.get("notification_cooldown", 60)
        if current_time - self.last_notification_time < cooldown:
            return
            
        try:
            timeout = 10 if level != "critical" else 30
            notification.notify(
                title=title[:64],  # Some platforms limit title length
                message=message[:256],  # Limit message length
                timeout=timeout,
                app_name="Memory Guardian"
            )
            self.last_notification_time = current_time
        except Exception as e:
            if self.config.get("enable_console", True):
                print(f"Notification error: {e}")
    
    def print_console(self, title: str, message: str, level: str):
        """Print alert to console."""
        if not self.config.get("enable_console", True):
            return
            
        icon = self.get_level_icon(level)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print()
        print("=" * 60)
        print(f"{icon} [{timestamp}] {title}")
        print("=" * 60)
        print(message)
        print("=" * 60)
        print()
    
    def check_once(self) -> dict:
        """Perform a single memory check."""
        usage, available_gb, total_gb, used_gb = self.get_memory_usage()
        level = self.get_level(usage)
        title, message = self.format_message(level, usage, available_gb)
        
        result = {
            "usage": usage,
            "available_gb": available_gb,
            "total_gb": total_gb,
            "used_gb": used_gb,
            "level": level,
            "title": title,
            "message": message
        }
        
        # Only alert if not normal
        if level != "normal":
            self.print_console(title, message, level)
            self.send_notification(title, message, level)
        
        return result
    
    def run_daemon(self):
        """Run in daemon mode with periodic checks."""
        interval = self.config.get("check_interval", 30)
        print(f"Memory Guardian started in daemon mode.")
        print(f"内存守护者已启动（守护模式）。")
        print(f"Check interval: {interval} seconds / 检查间隔: {interval} 秒")
        print()
        
        try:
            while True:
                result = self.check_once()
                if result["level"] == "normal":
                    # Only show minimal status for normal
                    icon = self.get_level_icon("normal")
                    print(f"{icon} Memory: {result['usage']:.1f}% | Available: {result['available_gb']:.1f} GB", end="\r")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n\nMemory Guardian stopped. / 内存守护者已停止。")
    
    def interactive_check(self):
        """Perform interactive check with cleanup option."""
        result = self.check_once()
        
        # Always show current status
        icon = self.get_level_icon(result["level"])
        print()
        print(f"{icon} 当前内存状态 / Current Memory Status")
        print(f"   使用率 / Usage: {result['usage']:.1f}%")
        print(f"   已用 / Used: {result['used_gb']:.1f} GB")
        print(f"   可用 / Available: {result['available_gb']:.1f} GB")
        print(f"   总计 / Total: {result['total_gb']:.1f} GB")
        print()
        
        if result["level"] in ["warning", "critical"]:
            print("是否查看可清理的进程？ (Y/N)")
            print("Show cleanable processes? (Y/N)")
            try:
                response = input("> ").strip().lower()
                if response in ["y", "yes", "是"]:
                    # Import and run cleanup
                    cleanup_script = Path(__file__).parent / "cleanup.py"
                    if cleanup_script.exists():
                        os.system(f'"{sys.executable}" "{cleanup_script}"')
                    else:
                        print("Cleanup script not found. / 清理脚本未找到。")
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled. / 已取消。")
        
        return result


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Memory Guardian - Cross-platform memory monitor / 内存守护者 - 跨平台内存监控"
    )
    parser.add_argument(
        "--check", "-c",
        action="store_true",
        help="Perform a single memory check / 执行单次内存检查"
    )
    parser.add_argument(
        "--daemon", "-d",
        action="store_true",
        help="Run in daemon mode with periodic checks / 守护模式运行"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to config file / 配置文件路径"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON / 以 JSON 格式输出"
    )
    
    args = parser.parse_args()
    
    guardian = MemoryGuardian(config_path=args.config)
    
    if args.daemon:
        guardian.run_daemon()
    elif args.check:
        result = guardian.check_once()
        if args.json:
            import json
            print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        # Default: interactive check
        guardian.interactive_check()


if __name__ == "__main__":
    main()
