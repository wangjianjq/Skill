---
tags: ["instrument", "r&s", "cmw500", "scpi", "rf-testing"]
---
# Skill: Rohde & Schwarz CMW500 (Radio Communication Tester)

## 1. Overview

The **CMW500** is a wideband radio communication tester for universal RF measurement.

* **Primary Roles**: Signal Generator (GPRF), LTE/5G Signaling, WLAN/Bluetooth Signaling.
* **Interface**: GPIB, LAN (VXI-11/HiSLIP), USB.

## 2. SCPI Command Basics (Standard Commands for Programmable Instruments)

* **Reset**: `*RST; *CLS` (Reset and Clear Status).
* **Identity**: `*IDN?` -> Returns `Rohde&Schwarz,CMW500...`.
* **Operation Complete**: `*OPC?` (Blocks until current operation finishes).

### GPRF (General Purpose RF Generator) Example

To generate a CW (Continuous Wave) signal:

```python
# 1. Select Generator Path 1
inst.write("ROUTe:GPRF:GEN:SCENario:SALone")

# 2. Set Frequency to 2.4 GHz
inst.write("SOURce:GPRF:GEN:RFSettings:FREQuency 2.4GHz")

# 3. Set Level to -10 dBm
inst.write("SOURce:GPRF:GEN:RFSettings:LEVel -10")

# 4. Turn Output ON
inst.write("SOURce:GPRF:GEN:STATe ON")
```

## 3. Automation Best Practices (Python/PyVISA)

1. **Timeout**: CMW operations (like boot-up or switching signaling modes) can be slow. Set `timeout=20000` (20s) or higher for signaling tasks.
2. **Error Checking**: After complex commands, query `SYSTem:ERRor?` to check for instrument errors.
3. **VXI-11 vs HiSLIP**: Prefer **HiSLIP** (`TCPIP0::...::hislip0::INSTR`) for faster LAN communication with R&S instruments.

## 4. Safety & Protection

* **Max Input Power**: Check the label (usually +30dBm for RF COM). **DO NOT EXCEED** or you will burn the frontend.
* **Cable Loss**: Always compensate for cable loss using `SCONfigure:EXTernal:CORRection`.
* **Thermal**: Ensure fan vents are not blocked.
