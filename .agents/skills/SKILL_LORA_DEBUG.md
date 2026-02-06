---
tags: ["hardware-comm", "lora", "lorawan", "sdr", "python"]
---
# Skill: LoRa / LoRaWAN Debugging

## 1. Overview

Protocol for debugging LoRa PHY and LoRaWAN Network layers.

## 2. Tools

* **PHY Layer**: SDR (RTL-SDR / HackRF) + GNU Radio / GQRX (Spectrum Analysis).
* **MAC Layer**: LoRaWAN Gateways (e.g., RAKwireless) + Packet Forwarder Logs.
* **Network Server**: ChirpStack / The Things Network (TTN) Console.
* **Python Libs**: `pylorawan` (Parsing), `sx126x` (Hardware Control).

## 3. Python Parsing Utility

```python
import base64
from lorawan.message import Message

# Example Base64 payload from Gateway
raw = "QAEBAQGAAAABAwAAAA=="
data = base64.b64decode(raw)

msg = Message(data)
print(f"DevAddr: {msg.mac_payload.fhdr.dev_addr}")
print(f"FCnt: {msg.mac_payload.fhdr.fcnt}")
```

## 4. Debugging Workflow

1. **Spectrum Check**: Use SDR + GQRX to verify 868/915MHz signal presence and integrity (Chirp structure).
2. **Gateway Logs**: Check if Gateway receives packets (CRC OK?).
3. **Server Logs**: Check Join Request/Accept flow in TTN/ChirpStack console.
4. **Decrypt**: Use AppSKey/NwkSKey to decrypt payloads if needed.
