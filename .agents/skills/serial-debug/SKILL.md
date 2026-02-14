---
tags: ["hardware", "debugging", "serial", "uart", "i2c", "spi"]
---
# Skill: Serial Debugging & Hardware Communication Standards

## 1. UART (Universal Asynchronous Receiver/Transmitter)

* **Standard Config**: 115200 8N1 (8 bits, No parity, 1 stop bit).
* **Debugging Logic**:
  * **Garbage Characters?**: Baud rate mismatch or clock drift (check internal RC oscillator).
  * **TX but no RX?**: Check TX/RX swap.
  * **Missing Data?**: Buffer overflow. Use DMA or ring buffers for non-blocking logging.

## 2. I2C (Inter-Integrated Circuit)

* **Pull-ups**: Ensure SDA/SCL have 4.7k - 10k resistors to VCC.
* **Scanning**: Use an I2C scanner script to verify slave address (7-bit vs 8-bit notation).
* **Stuck Bus**: If SDA is stuck LOW, clock the SCL 9 times manually to reset slave state.
* **Speed**: Start at 100kHz (Standard Mode) before attempting 400kHz (Fast Mode).

## 3. SPI (Serial Peripheral Interface)

* **Mode**: Verify CPOL/CPHA settings (Modes 0-3). Incorrect mode causes bit-shifted data.
* **Chip Select (CS)**: Must be pulled LOW for the duration of the entire frame.
* **Signal Integrity**: For long leads, reduce clock speed.

## 4. Hardware Safety & Probing

* **Common Ground**: MUST connect logic analyzer ground to target ground.
* **Voltage Levels**: Ensure 3.3V vs 5V compatibility. Use level shifters if necessary.
* **Logic Analyzer**: Prefer PulseView/Sigrok for protocol decoding over raw oscilloscope traces for complex transactions.
