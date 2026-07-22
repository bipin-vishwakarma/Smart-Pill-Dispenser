# Pill Dispenser V5 - Design Spec

## Board Specs
- Size: 70mm x 60mm
- Layers: 2-layer
- Components: All SMD (0603/0805)
- Finish: HASL lead-free

## Components (Simplified)

### Power Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| J1 | USB-C | TYPE-C-31-M-12 | Power input (5V) |
| U3 | TP4056 | SOIC-8 | Li-Ion charger |
| U4 | AP2112K-3.3 | SOT-23-5 | 3.3V LDO (600mA) |
| D3 | 1N5819 | SMA | Reverse polarity protection |
| J4 | JST-PH | 2-pin | Battery connector |
| C10 | 100µF | 0805 | Bulk capacitor |
| C1 | 10µF | 0805 | LDO input cap |
| C2 | 10µF | 0805 | LDO output cap |
| R5 | 2kΩ | 0603 | Charge current set (RProg) |
| R11 | 5.1kΩ | 0603 | CC1 pull-down (USB-C) |
| R12 | 5.1kΩ | 0603 | CC2 pull-down (USB-C) |

### Microcontroller Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| U1 | ESP32-S3-WROOM-1 | RF_Module | Main MCU |
| C5 | 100nF | 0603 | VDD bypass |
| C6 | 100nF | 0603 | VDD bypass |
| C7 | 100nF | 0603 | VDD bypass |
| C8 | 100nF | 0603 | VDD bypass |
| C9 | 10µF | 0805 | Bulk cap |
| R8 | 10kΩ | 0603 | BOOT pull-up (GPIO0) |
| R17 | 10kΩ | 0603 | EN pull-up |
| SW1 | BOOT | 6mm SMD | Boot button |
| SW2 | RESET | 6mm SMD | Reset button |

### User Interface Section
| Ref | Value | Package | Purpose |
|-----|-------|---------|---------|
| J3 | OLED | 4-pin header | I2C display (GPIO4=SDA, GPIO5=SCL) |
| J2 | SERVO | 3-pin header | Servo control (GPIO9=PWM) |
| BZ1 | Buzzer | 12x9.5mm SMD | Audio feedback |
| Q1 | MMBT2222A | SOT-23 | Buzzer transistor |
| D1 | Red | 0805 | Status LED |
| D4 | Red | 0805 | Charge LED |
| D5 | Green | 0805 | Standby LED |
| R1 | 330Ω | 0603 | D1 resistor |
| R2 | 330Ω | 0603 | D4 resistor |
| R3 | 330Ω | 0603 | D5 resistor |
| R4 | 1kΩ | 0603 | Q1 base resistor |
| SW3 | USER | 6mm SMD | User button (GPIO12) |
| R6 | 4.7kΩ | 0603 | I2C SDA pull-up |
| R7 | 4.7kΩ | 0603 | I2C SCL pull-up |
| R9 | 100kΩ | 0603 | Battery ADC divider (GPIO34) |
| R10 | 100kΩ | 0603 | Battery ADC divider |

## GPIO Assignments
| GPIO | Function | Notes |
|------|-----------|-------|
| GPIO0 | BOOT | Button with R8 pull-up |
| GPIO4 | I2C SDA | OLED display |
| GPIO5 | I2C SCL | OLED display |
| GPIO9 | Servo PWM | Servo motor control |
| GPIO10 | Buzzer | Via Q1 transistor |
| GPIO11 | Status LED | D1 |
| GPIO12 | User Button | SW3 |
| GPIO34 | Battery ADC | Via R9/R10 divider |

## Power Architecture
```
USB-C (5V) ──┬──► TP4056 (charger) ──► Battery
              │
              └──► AP2112K-3.3 ──► 3.3V ──► ESP32
```

## Zone Layout (70x60mm)
```
+----------------------+----------------------+
|    POWER (25x30)    |   ESP32 (25x30)      |
|   USB-C, TP4056     |   WROOM-1             |
|   LDO, Battery       |   Keepout            |
|   Caps, Diodes      |   Caps               |
+----------------------+----------------------+
|    UI (35x30)        |   OUTPUT (20x30)     |
|   Buttons, LEDs      |   OLED, Servo         |
|   Buzzer            |   Connectors         |
+----------------------+----------------------+
```

## Acceptance Criteria
- [ ] Schematic complete, clean, labeled
- [ ] ERC: 0 errors
- [ ] PCB: 70x60mm outline
- [ ] All components SMD
- [ ] DRC: 0 errors
- [ ] Gerbers ready for manufacturing