---
tags: ["instrument", "logic-analyzer", "saleae", "python-api", "debugging"]
---
# Skill: Saleae Logic Analyzer (Automation)

## 1. Overview

The industry standard for digital signal debugging and protocol decoding.

* **Primary Roles**: I2C/SPI/UART/CAN decoding, timing verification.
* **Interface**: USB 3.0.
* **Control Lib**: `saleae` (Logic 1.x) or `logic2-automation` (Logic 2.x). Note: Logic 2 API is preferred.

## 2. Automation Logic (Logic 2 gRPC API)

Using the `saleae-logic2-automation` python package.

```python
from saleae import automation
import os.path

# Connect to running Logic 2 application
with automation.Manager.connect(port=10430) as manager:
    
    # Configure Capture
    device_configuration = automation.LogicDeviceConfiguration(
        enabled_digital_channels=[0, 1, 2, 3],
        digital_sample_rate=10_000_000, # 10 MS/s
        digital_threshold_volts=1.2
    )

    capture_configuration = automation.CaptureConfiguration(
        capture_mode=automation.TimedCaptureMode(duration_seconds=5.0)
    )

    # Start Capture
    with manager.start_capture(
        device_configuration=device_configuration,
        capture_configuration=capture_configuration
    ) as capture:
        
        capture.wait()

        # Save to file
        capture.save_capture(filepath=os.path.abspath("capture_test.sal"))
        
        # Export Raw Data (CSV)
        capture.export_raw_data_csv(
            directory=os.path.abspath("output_csv"),
            digital_channels=[0, 1]
        )
```

## 3. Triggering

Automation is useless without precise triggering.

* You generally set up the trigger in the GUI for complex cases, or use simple digital edge triggers via API.
* For advanced CI/CD, use a **GPIO sync line** from the DUT to Channel 0 of Saleae to start recording exactly when the test starts.
