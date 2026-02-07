---
tags: ["instrument", "dmm", "multimeter", "scpi", "measure", "logging"]
---
# Skill: Digital Multimeter (SCPI)

## 1. Overview

High-precision measurement for voltage, current, resistance (e.g., Keysight 34461A, Keithley 2000).

* **Primary Roles**: Static Power consumption check, Precision voltage rail check.
* **Interface**: USB, LAN, GPIB.

## 2. Common Configurations

* **DC Voltage**: `CONF:VOLT:DC 10, 0.0001` (Range 10V, Resolution 100uV).
* **DC Current**: `CONF:CURR:DC AUTO` (Auto-range).
* **Input Impedance**: `INPut:IMPedance:AUTO ON` (Useful for measuring weak signals >10G Ohm).

## 3. Data Logging Script (PyVISA)

```python
import pyvisa
import time

rm = pyvisa.ResourceManager()
dmm = rm.open_resource('TCPIP0::...::INSTR')

# Setup for fast sampling
dmm.write("*RST")
dmm.write("CONF:VOLT:DC AUTO")
dmm.write("SAMP:COUN 10") # Take 10 samples per trigger

triggered_data = dmm.query("READ?") # READ? initiates trigger and fetches
print(f"Readings: {triggered_data}")
```

## 4. Current Measurement Shunt Warning

* **Burden Voltage**: When measuring current, the DMM adds a series resistance (shunt). On low-voltage rails (e.g., 1.8V), this voltage drop can crash the DUT.
* **Solution**: Use a dedicated Source Measure Unit (SMU) or power analyzer for ultra-low voltage/current rails.
