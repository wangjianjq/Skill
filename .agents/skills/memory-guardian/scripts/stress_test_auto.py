#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memory Stress Test (Auto) - 自动内存压力测试
无需交互，自动分配内存并保持运行
"""

import sys
import time
import gc
import os
import signal

try:
    import psutil
except ImportError:
    print("Error: psutil is required for memory pre-check. Run: pip install psutil")
    sys.exit(1)

def signal_handler(sig, frame):
    """处理终止信号"""
    print("\n[Stress Test] 接收到终止信号，正在释放内存...")
    sys.exit(0)

# 注册信号
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def main():
    target_gb = 7.0  # 默认分配 7GB 内存
    if len(sys.argv) > 1:
        try:
            target_gb = float(sys.argv[1])
        except ValueError:
            print(f"⚠️  无效的内存数值，使用默认值 {target_gb} GB")
    
    # 边界值检查：获取当前可用物理内存
    available_mem = psutil.virtual_memory().available / (1024 ** 3)
    total_mem = psutil.virtual_memory().total / (1024 ** 3)
    
    print(f"[Stress Test] 系统总内存: {total_mem:.2f} GB")
    print(f"[Stress Test] 当前可用内存: {available_mem:.2f} GB")
    
    if target_gb > available_mem:
        print(f"❌ 错误: 请求分配 {target_gb} GB，但可用内存仅剩 {available_mem:.2f} GB")
        print("   为避免系统崩溃，操作已终止。")
        sys.exit(1)
    
    if target_gb <= 0:
        print("❌ 错误: 分配内存必须大于 0")
        sys.exit(1)

    print(f"[Stress Test] 开始分配 {target_gb} GB 内存...")
    
    chunks = []
    chunk_size = 100 * 1024 * 1024  # 100 MB
    num_chunks = int(target_gb * 10.24)
    
    for i in range(num_chunks):
        try:
            chunks.append(bytearray(chunk_size))
            print(f"  已分配 / Allocated: {(i+1) * 100} MB ({(i+1)*100/1024:.1f} GB)", end="\r")
            time.sleep(0.1)  # 慢慢分配，方便观察
        except MemoryError:
            print(f"\n  内存不足 / Out of memory")
            break
    
    actual_mb = len(chunks) * 100
    print(f"\n✅ 已分配 {actual_mb} MB ({actual_mb/1024:.1f} GB)")
    print("进程保持运行中... PID:", os.getpid() if 'os' in dir() else "N/A")
    print("Ctrl+C 或使用 cleanup.py 终止")
    print(f"PID: {os.getpid()}")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n释放内存...")
        del chunks
        gc.collect()

if __name__ == "__main__":
    main()
