# Pill Dispenser V4 - Target Document

## Project Overview
Automatic pill dispenser with rotating compartment, powered by ESP32-S3-WROOM-1 with Li-Ion battery and USB-C charging.

## Board Specifications
- **Size**: 50mm x 40mm (compact)
- **Layers**: 2-layer PCB
- **Components**: All SMD (0603/0805)
- **Finish**: HASL lead-free

## Power Architecture
- USB-C input: 5V VBUS
- TP4056: Li-Ion charging IC
- AP2112K-3.3: 3.3V LDO (600mA)
- Battery: JST-PH 2-pin connector

## Components List

### Power Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| J1 | USB-C | TYPE-C-31-M-12 | Power input |
| U3 | TP4056 | SOIC-8 | Charger IC |
| U4 | AP2112K-3.3 | SOT-23-5 | 3.3V LDO |
| D3 | 1N5819 | SMA | Reverse polarity protection |
| J4 | JST-PH | 2-pin | Battery connector |
| SW4 | EG1224 | SPDT | Power switch |
| C10 | 100µF | 0805 | Bulk cap |
| C1 | 10µF | 0805 | LDO input |
| C2 | 10µF | 0805 | LDO output |
| R5 | 2kΩ | 0603 | Charge current set |
| R11 | 5.1kΩ | 0603 | CC1 pull-down |
| R12 | 5.1kΩ | 0603 | CC2 pull-down |
| R15 | 22Ω | 0603 | D+ series |
| R16 | 22Ω | 0603 | D- series |

### Microcontroller Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| U1 | ESP32-S3-WROOM-1 | RF_Module | Main MCU |
| C5-C8 | 100nF | 0603 | VDD bypass |
| C9 | 10µF | 0805 | Bulk cap |
| R8 | 10kΩ | 0603 | BOOT pull-up |
| R17 | 10kΩ | 0603 | EN pull-up |
| SW2 | 6mm | SW_PUSH | BOOT button |
| SW3 | 6mm | SW_PUSH | RESET button |

### User Interface Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| J3 | 4-pin | 1x04 | OLED I2C |
| J2 | 3-pin | 1x03 | Servo connector |
| BZ1 | 5020 | SMD | Buzzer |
| Q1 | MMBT2222A | SOT-23 | Buzzer driver |
| D1 | Red | 0805 | Status LED |
| D4 | Red | 0805 | Charge LED |
| D5 | Green | 0805 | Standby LED |
| R1,R2,R13,R14 | 330Ω | 0603 | LED resistors |
| R4 | 1kΩ | 0603 | Q1 base |
| SW1 | 6mm | SW_PUSH | User button |
| R6,R7 | 4.7kΩ | 0603 | I2C pull-ups |
| R9,R10 | 100kΩ | 0603 | Battery divider |

## Layout Zones (50x40mm)
```
+------------------+------------------+
|   POWER (20x20)  |   ESP32 (20x20)  |
|   USB-C, TP4056  |   WROOM-1        |
|   LDO, Battery   |   Keepout        |
+------------------+------------------+
|    UI (25x20)    |   PERIPH (25x20) |
| Buttons, LEDs    | Servo, Connectors|
+------------------+------------------+
```

## GPIO Assignments
- GPIO0: BOOT button
- GPIO4: I2C SDA (OLED)
- GPIO5: I2C SCL (OLED)
- GPIO9: Servo PWM
- GPIO10: Buzzer (via Q1)
- GPIO11: Status LED
- GPIO12: User button
- GPIO19: USB D-
- GPIO20: USB D+
- GPIO34: Battery ADC

## Acceptance Criteria
- [ ] Schematic complete with all nets labeled
- [ ] ERC: 0 errors
- [ ] PCB: 50x40mm outline
- [ ] All components SMD
- [ ] DRC: 0 errors, 0 unconnected
- [ ] Gerbers ready for JLCPCB