---
tags: ["hardware-comm", "usb", "python", "wireshark"]
---
# Skill: USB Debugging & Automation

## 1. Overview

Protocol for debugging USB devices using software sniffers and Python automation.

## 2. Tools

* **Analysis**: Wireshark with USBPcap (Windows) or usbmon (Linux).
* **Automation**: Python `pyusb` (libusb wrapper).
* **Hardware**: Total Phase Beagle (High-end) or OpenVizsla (Open-source).

## 3. Python Automation (PyUSB)

```python
import usb.core
import usb.util

# Find device
dev = usb.core.find(idVendor=0x1234, idProduct=0x5678)

if dev is None:
    raise ValueError('Device not found')

# Set configuration to first available
dev.set_configuration()

# Write to Endpoint 1 (OUT)
dev.write(1, b'\x00\x01\x02')

# Read from Endpoint 129 (IN)
data = dev.read(0x81, 64)
print(data)
```

## 4. Debugging Workflow

1. **Capture**: Start Wireshark with USBPcap.
2. **Plug & Play**: Connect device, perform actions.
3. **Analyze**: Filter by `usb.addr` to isolate device traffic.
4. **Replay**: Use `pyusb` to mimic host commands verifying device response.
