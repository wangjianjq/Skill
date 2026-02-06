---
tags: ["instrument", "power-supply", "scpi", "keysight", "rigol"]
---
# Skill: Programmable DC Power Supply (SCPI)

## 1. Overview

Standard control for T&M power supplies (e.g., Keysight E36300, Rigol DP800).

* **Primary Roles**: Automated DUT power cycling, Current consumption profiling.
* **Interface**: USB, LAN (LXI), GPIB.

## 2. Common SCPI Commands

* **Channel Select**: `INSTrument:SELect CH1`
* **Set Voltage/Current**:
  * `APPLy CH1, 3.3, 0.5` (Set CH1 to 3.3V, 0.5A limit).
  * `VOLTage 3.3; CURRent 0.5` (Component command style).
* **Output Control**:
  * `OUTPut ON` / `OUTPut OFF`.

## 3. Automation Example (PyVISA)

```python
import pyvisa
import time

rm = pyvisa.ResourceManager()
psu = rm.open_resource('USB0::...')

# 1. Reset
psu.write("*RST")

# 2. Configure Channel 1 to 3.3V, 1.0A
psu.write("INST CH1")
psu.write("VOLT 3.3")
psu.write("CURR 1.0")

# 3. Turn On
psu.write("OUTP ON")

# 4. Measure Actual Voltage/Current
meas_v = float(psu.query("MEAS:VOLT?"))
meas_i = float(psu.query("MEAS:CURR?"))
print(f"V: {meas_v:.3f}V, I: {meas_i:.4f}A")
```

## 4. OVP/OCP Protection

Always set Over-Voltage Protection (OVP) to prevent frying the DUT if the PSU glitches.

* `VOLTage:PROTection 3.6` (Trip if > 3.6V).
* `VOLTage:PROTection:STATe ON`.
