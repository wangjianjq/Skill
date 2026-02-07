---
tags: ["instrument", "anritsu", "mt8820c", "mt8821c", "wireless", "scpi"]
---
# Skill: Anritsu MT8820C/MT8821C (Radio Comm Analyzer)

## 1. Overview

The industry standard for 2G/3G/4G manufacturing and R&D testing.

* **Primary Roles**: LTE/WCDMA/GSM Calibration & Non-Signaling Test.
* **Interface**: GPIB (most common in factories), LAN.

## 2. SCPI Command Style

Anritsu commands are often short and specific to the measurement mode.

* **Mode Select**: `STDSEL LTE`
* **Measure Tx Power**: `SWP` (Start Wireless Power measurement) -> `FETCH:TXP?`

## 3. Parallel Phone Testing (PPT)

The MT8821C supports testing 2 phones simultaneously.

* **Select Phone 1**: `ANALOG` (or specific port selection command).
* **Select Phone 2**: `ANALOG2`.

## 4. Critical Logic

1. **Fast Switch**: Use list mode or fast switch commands for calibration routines to save ms.
2. **Calibration**: Ensure cable loss tables (`LOSSTABLE`) are loaded for specific frequency bands.
3. **Legacy Handling**: The older MT8820C has a slower processor; avoid flooding it with commands. Add small delays (10ms) if automation fails.
