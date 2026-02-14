---
tags: ["instrument", "debug-probe", "j-link", "swd", "jtag", "pylink"]
---
# Skill: Segger J-Link (JTAG/SWD Probe)

## 1. Overview

The gold standard for ARM Cortex-M/A debugging and flashing.

* **Primary Roles**: Firmware Flashing, RTT (Real-Time Transfer) Logging, Core Control.
* **Interface**: USB, Ethernet (Pro/WiFi models).

## 2. J-Link Commander (CLI)

Quick scripts often use the `JLink.exe` command line.

* `connect`: Connect to target used in script.
* `loadfile <firware.hex>`: Flash firmware.
* `r`: Reset target.
* `g`: Go (Run).

## 3. Python Automation (pylink-square)

Using the `pylink` library for complex test logic.

```python
import pylink

jlink = pylink.JLink()
jlink.open()
jlink.connect('STM32F407VG') # Set Target Device

# 1. Flash Firmware
jlink.flash_file('firmware.bin', 0x08000000)

# 2. Reset & Run
jlink.reset()
jlink.restart()

# 3. Read RTT Log (High Speed Logging)
# Requires RTT block address or auto-detection
try:
    jlink.rtt_start()
    while True:
        data = jlink.rtt_read(0, 1024)
        if data:
            print("".join(map(chr, data)), end="")
except KeyboardInterrupt:
    pass
```

## 4. Recovering "Bricked" Chips

* **Connect under Reset**: If the MCU goes to sleep immediately, use `connect` in J-Link Commander and allow it to hold the RESET pin low (`under-reset`) to regain control.
