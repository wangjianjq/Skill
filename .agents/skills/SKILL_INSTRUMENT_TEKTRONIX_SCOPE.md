---
tags: ["instrument", "tektronix", "oscilloscope", "mdo", "mso", "scpi"]
---
# Skill: Tektronix Oscilloscopes (MDO/MSO Series)

## 1. Overview

Standard protocol for Tektronix Mixed Domain (MDO) and Mixed Signal (MSO) oscilloscopes.

* **Primary Roles**: Signal integrity, timing analysis, protocol decoding, RF spectrum analysis (MDO).
* **Interface**: USBTMC, LAN (VXI-11), Socket.

## 2. Common SCPI Commands

* **Autoset**: `AUTOSet EXECute` (Use sparingly in automation).
* **Acquisition**:
  * Start: `ACQuire:STATE ON`
  * Stop: `ACQuire:STATE OFF`
  * Number of Points: `HORizontal:RECOrdlength 10000`

## 3. Data Transfer (Waveform Fetching)

Transferring waveform data is the most critical task.

```python
# 1. Set Data Source
inst.write("DATa:SOUrce CH1")
# 2. Set Encoding (Fastest)
inst.write("DATa:ENCdg RIBinary") 
inst.write("WFMOutpre:BYT_Nr 1") 

# 3. Request Curve
raw_data = inst.query_binary_values('CURVe?', datatype='b', is_big_endian=True)
```

## 4. Best Practices

1. **Wait for Event**: Use `*OPC?` after changing timebase/trigger settings to ensure the scope has settled.
2. **Display OFF**: `DISplay:GLObal:STATE OFF` improves update rate during heavy remote control.
3. **Error Queue**: Tek scopes can get stuck if the error queue fills up. Clear with `*CLS` at start.
