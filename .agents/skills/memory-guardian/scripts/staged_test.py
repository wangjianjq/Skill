#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memory Staged Stress Test - 阶梯式内存压力测试
逐步增加内存到各个阈值，测试 Memory Guardian 各级别警告
"""

import sys
import time
import gc
import os

try:
    import psutil
except ImportError:
    print("需要安装 psutil: pip install psutil")
    sys.exit(1)

def get_memory_info():
    """获取当前内存信息"""
    mem = psutil.virtual_memory()
    return {
        "percent": mem.percent,
        "available_gb": mem.available / (1024**3),
        "total_gb": mem.total / (1024**3),
        "used_gb": mem.used / (1024**3)
    }

def allocate_to_target(current_chunks, target_percent, chunk_size_mb=100):
    """分配内存直到达到目标百分比"""
    chunk_size = chunk_size_mb * 1024 * 1024
    
    while True:
        mem = get_memory_info()
        if mem["percent"] >= target_percent:
            break
        try:
            current_chunks.append(bytearray(chunk_size))
            print(f"  分配中: {len(current_chunks) * chunk_size_mb} MB | 当前: {mem['percent']:.1f}%", end="\r")
            time.sleep(0.05)
        except MemoryError:
            print(f"\n  ⚠️ 内存不足")
            break
    
    print()
    return current_chunks

def release_all(chunks):
    """释放所有内存"""
    del chunks[:]
    gc.collect()
    time.sleep(1)

def main():
    print()
    print("=" * 65)
    print("🧪 阶梯式内存压力测试 / Staged Memory Stress Test")
    print("=" * 65)
    print()
    print("此测试将逐步增加内存使用率到各个警告阈值：")
    print("This test will gradually increase memory to each threshold:")
    print("  🟡 70% - 注意 / Notice")
    print("  🟠 80% - 警告 / Warning")
    print("  🔴 90% - 严重 / Critical")
    print()
    print(f"当前 PID: {os.getpid()}")
    print()
    
    mem = get_memory_info()
    print(f"初始状态: 使用率 {mem['percent']:.1f}% | 可用 {mem['available_gb']:.1f} GB")
    print()
    print("-" * 65)
    
    chunks = []
    thresholds = [
        (70, "🟡 注意级别 / Notice Level"),
        (80, "🟠 警告级别 / Warning Level"),
        (90, "🔴 严重级别 / Critical Level")
    ]
    
    for target, label in thresholds:
        mem = get_memory_info()
        if mem["percent"] >= target:
            print(f"\n当前已超过 {target}%，跳过...")
            continue
            
        print()
        print(f">>> 测试 {label} (目标: {target}%)")
        print("-" * 65)
        
        # 分配内存到目标
        chunks = allocate_to_target(chunks, target)
        
        mem = get_memory_info()
        print(f"✅ 已达到目标: {mem['percent']:.1f}%")
        print(f"   已分配: {len(chunks) * 100} MB")
        print()
        print(">>> 请在另一个终端运行以下命令查看警告：")
        print("    python .agents/skills/memory-guardian/scripts/monitor.py --check")
        print()
        print(f"按 Enter 继续下一阶段，或输入 'r' 释放内存，'q' 退出...")
        
        try:
            choice = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n退出...")
            break
            
        if choice == 'q':
            break
        elif choice == 'r':
            print("释放内存...")
            release_all(chunks)
            chunks = []
            mem = get_memory_info()
            print(f"✅ 已释放，当前: {mem['percent']:.1f}%")
    
    print()
    print("-" * 65)
    print("测试结束 / Test Complete")
    print()
    
    if chunks:
        print(f"当前仍有 {len(chunks) * 100} MB 内存被占用")
        print("按 Enter 释放并退出，或 Ctrl+C 保持运行...")
        try:
            input()
            release_all(chunks)
            print("✅ 内存已释放")
        except KeyboardInterrupt:
            print("\n保持运行中... 使用 cleanup.py 终止")
            while True:
                time.sleep(10)

if __name__ == "__main__":
    main()

