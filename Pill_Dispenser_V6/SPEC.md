# Pill Dispenser V6 - FINAL SPEC

## Board Overview
- **Size**: 70mm x 50mm (fits pill dispenser)
- **Layers**: 2-layer PCB
- **Components**: All SMD (0603/0805)
- **Finish**: HASL lead-free

## Power Architecture
```
USB-C (5V) ──┬──► TP4056 ──► Battery (Li-Ion)
              │
              └──► AP2112K-3.3 ──► 3.3V ──► ESP32

ESP32 ──► OLED Display (I2C)
       ──► Servo Motor (PWM)
       ──► Buzzer (Audio)
       ──► LEDs (Status)
       ──► Buttons (User Input)
```

## Component Placement Zones
```
+------------------------+----------------------+
|      POWER ZONE        |     ESP32 ZONE      |
|   (Top-Left 30x25mm)  |  (Top-Right 30x25mm)|
|                        |                      |
|  USB-C  TP4056  LDO    |  ESP32-S3-WROOM-1  |
|  Battery  Schottky     |  Keepout Area       |
|  Power Caps            |  Bypass Caps        |
+------------------------+----------------------+
|      UI ZONE           |    OUTPUT ZONE      |
|   (Bottom-Left 30x25mm)| (Bottom-Right 30x25)|
|                        |                      |
|  Buttons  LEDs         |  OLED Connector     |
|  Status LEDs           |  Servo Connector    |
|  Buzzer                |                     |
+------------------------+----------------------+
```

## Component List

### Power Section
| Ref | Component | Value | Footprint |
|-----|-----------|-------|-----------|
| J1 | USB-C | USB-C | USB_C_Receptacle_USB2.0_16P |
| U3 | TP4056 | Li-Ion Charger | SOIC-8 |
| U4 | AP2112K-3.3 | 3.3V LDO | SOT-23-5 |
| D3 | 1N5819 | Schottky Diode | SMA |
| J4 | Battery | JST 2-pin | Conn_01x02 |
| C10 | Capacitor | 100µF | Capacitor_THT |
| C1 | Capacitor | 10µF | 0805 |
| C2 | Capacitor | 10µF | 0805 |
| R11 | Resistor | 5.1kΩ | 0603 |
| R12 | Resistor | 5.1kΩ | 0603 |

### MCU Section  
| Ref | Component | Value | Footprint |
|-----|-----------|-------|-----------|
| U1 | ESP32-S3-WROOM-1 | MCU Module | RF_Module |
| C5 | Capacitor | 100nF | 0603 |
| C6 | Capacitor | 100nF | 0603 |
| C7 | Capacitor | 100nF | 0603 |
| C8 | Capacitor | 100nF | 0603 |
| C9 | Capacitor | 10µF | 0805 |
| R8 | Resistor | 10kΩ | 0603 |
| R17 | Resistor | 10kΩ | 0603 |
| SW2 | Button | RESET | SW_Push |
| SW3 | Button | BOOT | SW_Push |

### UI Section
| Ref | Component | Value | Footprint |
|-----|-----------|-------|-----------|
| SW1 | Button | USER | SW_Push |
| D1 | LED | Red (Status) | 0805 |
| D4 | LED | Red (Charge) | 0805 |
| D5 | LED | Green (Standby) | 0805 |
| BZ1 | Buzzer | 12x9.5mm | SMD |
| Q1 | MMBT2222A | NPN Transistor | SOT-23 |
| R1 | Resistor | 330Ω | 0603 |
| R2 | Resistor | 330Ω | 0603 |
| R3 | Resistor | 330Ω | 0603 |
| R4 | Resistor | 1kΩ | 0603 |

### Output Section
| Ref | Component | Value | Footprint |
|-----|-----------|-------|-----------|
| J3 | OLED | 4-pin | Conn_01x04 |
| J2 | Servo | 3-pin | Conn_01x03 |
| R6 | Resistor | 4.7kΩ | 0603 |
| R7 | Resistor | 4.7kΩ | 0603 |
| R9 | Resistor | 100kΩ | 0603 |
| R10 | Resistor | 100kΩ | 0603 |

## GPIO Assignments
| GPIO | Function |
|------|----------|
| GPIO0 | BOOT Button |
| GPIO4 | I2C SDA (OLED) |
| GPIO5 | I2C SCL (OLED) |
| GPIO9 | Servo PWM |
| GPIO10 | Buzzer |
| GPIO11 | Status LED |
| GPIO12 | User Button |
| GPIO34 | Battery ADC |

## Design Rules (JLCPCB)
- Min trace width: 0.127mm (5mil)
- Min clearance: 0.127mm
- Min via drill: 0.3mm
- Min via diameter: 0.6mm
- Copper pour clearance: 0.2mm

## Acceptance Criteria
- [ ] Schematic complete with all connections
- [ ] ERC: 0 errors
- [ ] PCB: 70x50mm
- [ ] Proper component placement by zone
- [ ] DRC: 0 errors
- [ ] Ground planes on both layers
- [ ] Gerbers generated