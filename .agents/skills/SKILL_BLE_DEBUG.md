---
tags: ["hardware-comm", "ble", "bluetooth", "python", "wireshark"]
---
# Skill: Bluetooth LE (BLE) Debugging

## 1. Overview

Protocol for analyzing and automating Bluetooth Low Energy (BLE) communication.

## 2. Tools

* **Sniffing**: Nordic nRF52840 Dongle + nRF Sniffer Firmware.
* **Analysis**: Wireshark with nRF Sniffer extcap plugin.
* **Automation**: Python `bleak` library (Cross-platform GATT client).

## 3. Python Automation (Bleak)

```python
import asyncio
from bleak import BleakClient

address = "AA:BB:CC:DD:EE:FF"
utils_uuid = "0000ffe0-0000-1000-8000-00805f9b34fb"

async def main():
    async with BleakClient(address) as client:
        # Write
        await client.write_gatt_char(utils_uuid, b"Hello World")
        
        # Read
        val = await client.read_gatt_char(utils_uuid)
        print(f"Received: {val}")

asyncio.run(main())
```

## 4. Debugging Workflow

1. **Sniff**: Plug in nRF dongle, start Wireshark, select nRF Sniffer interface.
2. **Filter**: Set Wireshark filter to the target MAC address.
3. **Interact**: Use mobile app or `bleak` script to trigger BLE operations.
4. **Analyze**: Inspect ATT/GATT packets for errors or timing issues.
