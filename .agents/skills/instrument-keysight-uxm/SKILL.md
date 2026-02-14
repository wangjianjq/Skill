---
tags: ["instrument", "keysight", "uxm", "5g", "scpi"]
---
# Skill: Keysight E7515B UXM (5G/LTE Wireless Test Platform)

## 1. Overview

The **UXM 5G** is Keysight's flagship network emulator for 5G NR and LTE signaling test.

* **Primary Roles**: 5G NR (SA/NSA) Signaling, LTE-A Pro Signaling, IMS/VoLTE/VoNR Test.
* **Interface**: LAN (HiSLIP/Socket), GPIB (Legacy).

## 2. SCPI Command Structure

Keysight SCPI is often tree-based and verbose.

* **Mode Switch**: `INSTrument:SELect "LTE"`, `INSTrument:SELect "NR5G"`
* **Cell Control (NR)**:
  * State ON: `BSE:CELL:NR5G:STATe 1`
  * Power: `BSE:CONFIG:NR5G:DL:POWer -50`

## 3. Python Control Example (PyVISA)

```python
import pyvisa

rm = pyvisa.ResourceManager()
# Use HiSLIP for high-speed data transfer
inst = rm.open_resource('TCPIP0::192.168.1.100::hislip0::INSTR')

# Query ID
print(inst.query("*IDN?"))

# Set Downlink Power to -70 dBm
inst.write("BSE:CONFIG:NR5G:DL:POWer -70")

# Check for Errors
print(inst.query("SYSTem:ERRor?"))
```

## 4. Key Considerations

1. **Application Switching**: Switching between LTE and 5G apps takes time (seconds to minutes). Always check `*OPC?`.
2. **Licensing**: Features are heavily license-dependent. Query `SYSTem:LICense:CATalog?` to check available features.
3. **Thermal**: The E7515B is a high-power chassis. Ensure enterprise-grade cooling in the rack.
