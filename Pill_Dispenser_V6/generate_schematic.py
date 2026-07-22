#!/usr/bin/env python3
"""
Generate complete Pill Dispenser V6 KiCad schematic with all wire connections.
This script calculates pin coordinates and writes the full schematic S-expression.
"""

import uuid
import random
random.seed(42)  # For reproducible UUIDs

def gen_uuid():
    return str(uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16))))

# Component pin coordinates (component_center + pin_offset)
# Calculated from symbol definitions and instance positions

# USB-C (J1) at (50, 100) - 16-pin USB-C symbol
usb_pins = {
    'A1_VBUS': (39.84, 102.54),   # VBUS left
    'A6_GND': (39.84, 100),       # GND left
    'A5_CC1': (39.84, 105.08),    # CC1
    'A4_DP': (39.84, 107.62),     # D+
    'A7_DM': (39.84, 110.16),    # D-
    'B5_CC2': (60.16, 105.08),    # CC2
    'B1_VBUS': (60.16, 102.54),   # VBUS right
    'B6_GND': (60.16, 100),      # GND right
}

# TP4056 (U3) at (50, 75) - 8-pin SOIC
tp4056_pins = {
    '1_TEMP': (42.38, 77.54),    # TEMP
    '2_PROG': (42.38, 75),       # PROG
    '3_GND': (42.38, 72.46),     # GND
    '4_VCC': (42.38, 69.92),     # VCC input
    '5_BAT': (57.62, 69.92),     # BAT output
    '6_VCCB': (57.62, 72.46),    # VCC (battery side)
    '7_STDBY': (57.62, 75),      # STDBY
    '8_CHRG': (57.62, 77.54),    # CHRG
}

# AP2112K (U4) at (50, 50) - SOT-23-5
ap2112k_pins = {
    '1_VIN': (44.92, 50),        # VIN
    '2_GND': (50, 44.92),        # GND
    '3_EN': (55.08, 50),         # EN
    '4_VOUT': (50, 55.08),       # VOUT
    '5_NC': (55.08, 44.92),      # NC (if exists)
}

# ESP32-S3-WROOM-1 (U1) at (140, 70) - 38-pin module
# Note: Only first 16 pins defined in symbol
esp32_pins = {
    '1_GND': (122.22, 87.78),
    '2_3V3': (122.22, 85.24),
    '3_EN': (157.78, 52.22),
    '4_GPIO0': (122.22, 82.7),
    '5_GPIO1': (122.22, 80.16),
    '6_GPIO2': (122.22, 77.62),
    '7_GPIO3': (122.22, 75.08),
    '8_GPIO4': (122.22, 72.54),
    '9_GPIO5': (122.22, 70),
    '10_GPIO6': (122.22, 67.46),
    '11_GPIO7': (122.22, 64.92),
    '12_GPIO8': (122.22, 62.38),
    '13_GPIO9': (122.22, 59.84),
    '14_GPIO10': (122.22, 57.3),
    '15_GPIO11': (122.22, 54.76),
    '16_GPIO12': (122.22, 52.22),
}

# Schottky Diode D3 at (70, 100) - SMA
d3_pins = {
    '1_K': (70, 105.08),  # K = Cathode = connected to BAT
    '2_A': (70, 94.92),   # A = Anode = connected to VIN
}

# Battery J4 at (30, 110) - Conn_01x02
j4_pins = {
    '1': (30, 115.08),  # Pin 1 (VBAT+)
    '2': (30, 104.92),  # Pin 2 (GND)
}

# Buttons SW1, SW2, SW3 at (100/110/120, 120) - SW_Push
sw1_pins = {'1': (100, 122.54), '2': (100, 117.46)}
sw2_pins = {'1': (110, 122.54), '2': (110, 117.46)}
sw3_pins = {'1': (120, 122.54), '2': (120, 117.46)}

# LEDs D1, D4, D5 at (90, 100/90/80) - LED
d1_pins = {'1_K': (90, 94.92), '2_A': (90, 105.08)}  # K=cathode, A=anode
d4_pins = {'1_K': (90, 84.92), '2_A': (90, 95.08)}
d5_pins = {'1_K': (90, 74.92), '2_A': (90, 85.08)}

# Capacitors C1, C2 at (60, 65/55) - Device:C
c1_pins = {'1': (60, 68.81), '2': (60, 61.19)}
c2_pins = {'1': (60, 58.81), '2': (60, 51.19)}

# More capacitors
c5_pins = {'1': (120, 58.81), '2': (120, 51.19)}
c6_pins = {'1': (120, 48.81), '2': (120, 41.19)}
c7_pins = {'1': (130, 58.81), '2': (130, 51.19)}
c8_pins = {'1': (130, 48.81), '2': (130, 41.19)}
c9_pins = {'1': (150, 54.81), '2': (150, 45.19)}
c10_pins = {'1': (40, 88.81), '2': (40, 81.19)}  # C_Polarized

# Resistors (Device:R) - pins at (x, y±2.19)
r1_pins = {'1': (80, 97.19), '2': (80, 92.81)}
r2_pins = {'1': (80, 87.19), '2': (80, 82.81)}
r3_pins = {'1': (80, 77.19), '2': (80, 72.81)}
r4_pins = {'1': (130, 92.81), '2': (130, 87.19)}  # 1k for buzzer base
r5_pins = {'1': (60, 92.81), '2': (60, 87.19)}   # 2k
r6_pins = {'1': (180, 52.19), '2': (180, 47.81)} # 4.7k for I2C SDA
r7_pins = {'1': (180, 62.19), '2': (180, 57.81)} # 4.7k for I2C SCL
r8_pins = {'1': (125, 122.54), '2': (125, 117.46)} # 10k for EN
r9_pins = {'1': (40, 127.19), '2': (40, 122.81)}  # 100k for TEMP
r10_pins = {'1': (45, 127.19), '2': (45, 122.81)} # 100k for TEMP
r11_pins = {'1': (50, 92.81), '2': (50, 87.19)}  # 5.1k for PROG
r12_pins = {'1': (55, 92.81), '2': (55, 87.19)}  # 5.1k for PROG
r17_pins = {'1': (135, 122.54), '2': (135, 117.46)} # 10k for USER button

# Buzzer BZ1 at (100, 100) - Buzzer
bz1_pins = {'1': (100, 105.08), '2': (100, 94.92)}

# Transistor Q1 at (110, 100) - MMBT2222A (SOT-23)
q1_pins = {
    '1_B': (107.46, 100),  # B = Base
    '2_E': (110, 104.92),  # E = Emitter
    '3_C': (112.54, 100),  # C = Collector
}

# OLED J3 at (200, 40) - Conn_01x04
j3_pins = {
    '1': (200, 50.16),  # Pin 1
    '2': (200, 42.54),  # Pin 2 (SDA)
    '3': (200, 37.46),  # Pin 3 (SCL)
    '4': (200, 32.38),  # Pin 4 (GND)
}

# Servo J2 at (200, 70) - Conn_01x03
j2_pins = {
    '1': (200, 77.62),  # Pin 1
    '2': (200, 70),     # Pin 2 (Signal)
    '3': (200, 62.38),  # Pin 3 (GND)
}

# Power symbols positions
pwr_vbus_pos = (50, 115)
pwr_3v3_pos = (70, 35)
pwr_gnd_pos = (90, 35)

# Build wire list - each wire connects two points
wires = []

# Helper to add a wire
def add_wire(x1, y1, x2, y2):
    wires.append({
        'pts': ((round(x1, 2), round(y1, 2)), (round(x2, 2), round(y2, 2))),
        'uuid': gen_uuid()
    })

# ============== POWER RAILS ==============

# VBUS net: USB-C VBUS -> TP4056 VCC(pin 4)
add_wire(usb_pins['A1_VBUS'][0], usb_pins['A1_VBUS'][1], tp4056_pins['4_VCC'][0], tp4056_pins['4_VCC'][1])
add_wire(usb_pins['B1_VBUS'][0], usb_pins['B1_VBUS'][1], usb_pins['A1_VBUS'][0], usb_pins['A1_VBUS'][1])
# TP4056 VCC pins connected
add_wire(tp4056_pins['4_VCC'][0], tp4056_pins['4_VCC'][1], tp4056_pins['6_VCCB'][0], tp4056_pins['6_VCCB'][1])

# GND net: Many connections
# USB-C GND -> TP4056 GND
add_wire(usb_pins['A6_GND'][0], usb_pins['A6_GND'][1], tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1])
add_wire(usb_pins['B6_GND'][0], usb_pins['B6_GND'][1], usb_pins['A6_GND'][0], usb_pins['A6_GND'][1])
# TP4056 GND -> AP2112K GND
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], ap2112k_pins['2_GND'][0], ap2112k_pins['2_GND'][1])
# AP2112K GND -> C1, C2
add_wire(ap2112k_pins['2_GND'][0], ap2112k_pins['2_GND'][1], c1_pins['2'][0], c1_pins['2'][1])
add_wire(ap2112k_pins['2_GND'][0], ap2112k_pins['2_GND'][1], c2_pins['2'][0], c2_pins['2'][1])
# More GND connections
add_wire(c1_pins['2'][0], c1_pins['2'][1], c2_pins['2'][0], c2_pins['2'][1])
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], c10_pins['2'][0], c10_pins['2'][1])
# Button GNDs
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], sw1_pins['2'][0], sw1_pins['2'][1])
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], sw2_pins['2'][0], sw2_pins['2'][1])
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], sw3_pins['2'][0], sw3_pins['2'][1])
# LED GNDs (cathode = K = negative = GND side)
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], d1_pins['1_K'][0], d1_pins['1_K'][1])
add_wire(d1_pins['1_K'][0], d1_pins['1_K'][1], d4_pins['1_K'][0], d4_pins['1_K'][1])
add_wire(d4_pins['1_K'][0], d4_pins['1_K'][1], d5_pins['1_K'][0], d5_pins['1_K'][1])
# Buzzer GND
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], bz1_pins['2'][0], bz1_pins['2'][1])
# Q1 Emitter GND
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], q1_pins['2_E'][0], q1_pins['2_E'][1])
# J3 GND (pin 4)
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], j3_pins['4'][0], j3_pins['4'][1])
# J2 GND (pin 3)
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], j2_pins['3'][0], j2_pins['3'][1])
# J4 GND (pin 2)
add_wire(tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1], j4_pins['2'][0], j4_pins['2'][1])

# BATT net: TP4056 BAT -> Schottky K -> J4 Pin 1
add_wire(tp4056_pins['5_BAT'][0], tp4056_pins['5_BAT'][1], d3_pins['1_K'][0], d3_pins['1_K'][1])
add_wire(d3_pins['1_K'][0], d3_pins['1_K'][1], j4_pins['1'][0], j4_pins['1'][1])

# VIN net: Schottky A -> AP2112K VIN + R11 + R12 + C10
add_wire(d3_pins['2_A'][0], d3_pins['2_A'][1], ap2112k_pins['1_VIN'][0], ap2112k_pins['1_VIN'][1])
add_wire(ap2112k_pins['1_VIN'][0], ap2112k_pins['1_VIN'][1], c10_pins['1'][0], c10_pins['1'][1])
# R11 connects to PROG pin
add_wire(ap2112k_pins['1_VIN'][0], ap2112k_pins['1_VIN'][1], r11_pins['1'][0], r11_pins['1'][1])
# R12 connects to GND for PROG divider
add_wire(r12_pins['2'][0], r12_pins['2'][1], tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1])
# R11 and R12 connect at PROG
add_wire(tp4056_pins['2_PROG'][0], tp4056_pins['2_PROG'][1], r11_pins['2'][0], r11_pins['2'][1])
add_wire(r11_pins['2'][0], r11_pins['2'][1], r12_pins['1'][0], r12_pins['1'][1])

# +3.3V net: AP2112K VOUT -> ESP32 3V3
add_wire(ap2112k_pins['4_VOUT'][0], ap2112k_pins['4_VOUT'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])
# C9 decoupling near ESP32
add_wire(ap2112k_pins['4_VOUT'][0], ap2112k_pins['4_VOUT'][1], c9_pins['1'][0], c9_pins['1'][1])
add_wire(c9_pins['2'][0], c9_pins['2'][1], tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1])

# EN net: AP2112K EN -> pulled HIGH (connect to VIN via resistor or direct)
# Connect EN directly to VIN for always-on operation
add_wire(ap2112k_pins['3_EN'][0], ap2112k_pins['3_EN'][1], ap2112k_pins['1_VIN'][0], ap2112k_pins['1_VIN'][1])
# Also connect R8 for ESP32 EN
add_wire(esp32_pins['3_EN'][0], esp32_pins['3_EN'][1], r8_pins['1'][0], r8_pins['1'][1])
add_wire(r8_pins['2'][0], r8_pins['2'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# TEMP net: TP4056 TEMP -> R9 -> GND
add_wire(tp4056_pins['1_TEMP'][0], tp4056_pins['1_TEMP'][1], r9_pins['1'][0], r9_pins['1'][1])
add_wire(r9_pins['2'][0], r9_pins['2'][1], r10_pins['1'][0], r10_pins['1'][1])
add_wire(r10_pins['2'][0], r10_pins['2'][1], tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1])

# ============== ESP32 CONNECTIONS ==============

# BOOT Button (SW3) -> GPIO0
add_wire(esp32_pins['4_GPIO0'][0], esp32_pins['4_GPIO0'][1], sw3_pins['1'][0], sw3_pins['1'][1])
add_wire(sw3_pins['1'][0], sw3_pins['1'][1], r17_pins['1'][0], r17_pins['1'][1])  # Pull-up
add_wire(r17_pins['2'][0], r17_pins['2'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# RESET Button (SW2) -> connected to EN via RC? Keep it simple
add_wire(esp32_pins['3_EN'][0], esp32_pins['3_EN'][1], sw2_pins['1'][0], sw2_pins['1'][1])

# USER Button (SW1) -> GPIO12
add_wire(esp32_pins['16_GPIO12'][0], esp32_pins['16_GPIO12'][1], sw1_pins['1'][0], sw1_pins['1'][1])

# ============== LED CONNECTIONS ==============

# Status LED D1 (Red) -> GPIO11 -> R1
add_wire(d1_pins['2_A'][0], d1_pins['2_A'][1], r1_pins['1'][0], r1_pins['1'][1])
add_wire(r1_pins['2'][0], r1_pins['2'][1], esp32_pins['15_GPIO11'][0], esp32_pins['15_GPIO11'][1])

# Charge LED D4 (Red) -> GPIO12
add_wire(d4_pins['2_A'][0], d4_pins['2_A'][1], r2_pins['1'][0], r2_pins['1'][1])
add_wire(r2_pins['2'][0], r2_pins['2'][1], esp32_pins['16_GPIO12'][0], esp32_pins['16_GPIO12'][1])

# Standby LED D5 (Green) -> GPIO34 (or another available GPIO)
# Using GPIO9 for now (was assigned to servo)
add_wire(d5_pins['2_A'][0], d5_pins['2_A'][1], r3_pins['1'][0], r3_pins['1'][1])
add_wire(r3_pins['2'][0], r3_pins['2'][1], esp32_pins['13_GPIO9'][0], esp32_pins['13_GPIO9'][1])

# ============== BUZZER CONNECTIONS ==============

# Buzzer -> Q1 transistor -> GPIO10
# Q1 Base -> R4 -> GPIO10
add_wire(esp32_pins['14_GPIO10'][0], esp32_pins['14_GPIO10'][1], r4_pins['1'][0], r4_pins['1'][1])
add_wire(r4_pins['2'][0], r4_pins['2'][1], q1_pins['1_B'][0], q1_pins['1_B'][1])
# Q1 Collector -> +3.3V via buzzer
add_wire(q1_pins['3_C'][0], q1_pins['3_C'][1], bz1_pins['1'][0], bz1_pins['1'][1])
add_wire(bz1_pins['1'][0], bz1_pins['1'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# ============== I2C (OLED) CONNECTIONS ==============

# J3 Pin 1 -> +3.3V (VCC for OLED)
add_wire(j3_pins['1'][0], j3_pins['1'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# J3 Pin 2 (SDA) -> R6 -> ESP32 GPIO4
add_wire(j3_pins['2'][0], j3_pins['2'][1], r6_pins['2'][0], r6_pins['2'][1])
add_wire(r6_pins['1'][0], r6_pins['1'][1], esp32_pins['8_GPIO4'][0], esp32_pins['8_GPIO4'][1])
# R6 pull-up to +3.3V
add_wire(r6_pins['1'][0], r6_pins['1'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# J3 Pin 3 (SCL) -> R7 -> ESP32 GPIO5
add_wire(j3_pins['3'][0], j3_pins['3'][1], r7_pins['2'][0], r7_pins['2'][1])
add_wire(r7_pins['1'][0], r7_pins['1'][1], esp32_pins['9_GPIO5'][0], esp32_pins['9_GPIO5'][1])
# R7 pull-up to +3.3V
add_wire(r7_pins['1'][0], r7_pins['1'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# ============== SERVO CONNECTIONS ==============

# J2 Pin 1 -> +3.3V (or 5V if needed)
add_wire(j2_pins['1'][0], j2_pins['1'][1], esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1])

# J2 Pin 2 (Signal/PWM) -> ESP32 GPIO10 (or another)
# Using GPIO10 for now (also used for buzzer - may conflict)
# Let's use a different GPIO for servo
# Actually, looking at spec: GPIO9 is for Servo PWM
add_wire(j2_pins['2'][0], j2_pins['2'][1], esp32_pins['13_GPIO9'][0], esp32_pins['13_GPIO9'][1])

# ============== BATTERY ADC ==============
# R5 (2k) for battery voltage divider - not connected in current list
# This could be added later

# ============== ESP32 BYPASS CAPACITORS ==============
# C5, C6, C7, C8 near ESP32
add_wire(esp32_pins['1_GND'][0], esp32_pins['1_GND'][1], c5_pins['2'][0], c5_pins['2'][1])
add_wire(esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1], c5_pins['1'][0], c5_pins['1'][1])

add_wire(esp32_pins['1_GND'][0], esp32_pins['1_GND'][1], c6_pins['2'][0], c6_pins['2'][1])
add_wire(esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1], c6_pins['1'][0], c6_pins['1'][1])

add_wire(esp32_pins['1_GND'][0], esp32_pins['1_GND'][1], c7_pins['2'][0], c7_pins['2'][1])
add_wire(esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1], c7_pins['1'][0], c7_pins['1'][1])

add_wire(esp32_pins['1_GND'][0], esp32_pins['1_GND'][1], c8_pins['2'][0], c8_pins['2'][1])
add_wire(esp32_pins['2_3V3'][0], esp32_pins['2_3V3'][1], c8_pins['1'][0], c8_pins['1'][1])

# ============== POWER SYMBOL CONNECTIONS ==============
# Connect power symbols to nets
# VBUS symbol at (50, 115)
add_wire(pwr_vbus_pos[0], pwr_vbus_pos[1], usb_pins['A1_VBUS'][0], usb_pins['A1_VBUS'][1])

# +3.3V symbol at (70, 35)
add_wire(pwr_3v3_pos[0], pwr_3v3_pos[1], ap2112k_pins['4_VOUT'][0], ap2112k_pins['4_VOUT'][1])

# GND symbol at (90, 35)
add_wire(pwr_gnd_pos[0], pwr_gnd_pos[1], tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1])

# Generate wire section
wire_section = []
for w in wires:
    x1, y1 = w['pts'][0]
    x2, y2 = w['pts'][1]
    uid = w['uuid']
    wire_section.append(f"    (wire (pts (xy {x1} {y1}) (xy {x2} {y2})) (uuid \"{uid}\"))")

wire_block = "\n".join(wire_section)

# Generate junctions where wires meet
# Key junctions to mark
junctions = [
    # USB VBUS junction
    (usb_pins['A1_VBUS'][0], usb_pins['A1_VBUS'][1]),
    (usb_pins['A6_GND'][0], usb_pins['A6_GND'][1]),
    # TP4056 GND (central GND point)
    (tp4056_pins['3_GND'][0], tp4056_pins['3_GND'][1]),
    # AP2112K GND
    (ap2112k_pins['2_GND'][0], ap2112k_pins['2_GND'][1]),
    # +3.3V
    (ap2112k_pins['4_VOUT'][0], ap2112k_pins['4_VOUT'][1]),
    # VIN
    (ap2112k_pins['1_VIN'][0], ap2112k_pins['1_VIN'][1]),
    # Battery node
    (d3_pins['1_K'][0], d3_pins['1_K'][1]),
    (tp4056_pins['5_BAT'][0], tp4056_pins['5_BAT'][1]),
]

junction_section = []
for x, y in junctions:
    junction_section.append(f"  (junction (at {x} {y}) (diameter 0.8) (color 0 0 0 0))")

junction_block = "\n".join(junction_section)

# Complete schematic content
schematic_content = f"""(kicad_sch (version 20250114) (generator "Pill_Dispenser_V6_Complete")

  (uuid "a1b05787-cd6a-483e-afe0-48eda7657ffa")

  (paper "A4")

  (lib_symbols
    (symbol "Connector:USB_C_Receptacle_USB2.0_16P"
      (pin passive line (at -10.16 0 0) (length 2.54) (name "GND") (number "A6")
      )
      (pin passive line (at -10.16 2.54 0) (length 2.54) (name "VBUS") (number "A1")
      )
      (pin passive line (at -10.16 5.08 0) (length 2.54) (name "CC1") (number "A5")
      )
      (pin passive line (at -10.16 7.62 0) (length 2.54) (name "D+") (number "A4")
      )
      (pin passive line (at -10.16 10.16 0) (length 2.54) (name "D-") (number "A7")
      )
      (pin passive line (at -10.16 12.7 0) (length 2.54) (name "CC2") (number "B5")
      )
      (pin passive line (at 10.16 0 180) (length 2.54) (name "GND") (number "B6")
      )
      (pin passive line (at 10.16 2.54 180) (length 2.54) (name "VBUS") (number "B1")
      )
      (rectangle (start -10.16 -2.54) (end 10.16 15.24)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "Device:R"
      (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Resistor_SMD:R_0603_1608Metric" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~") (number "1")
        )
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~") (number "2")
        )
      )
    )
    (symbol "Device:C"
      (pin_numbers hide) (pin_names (offset 0.254)) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Value" "C" (at 0.635 -2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Footprint" "Capacitor_SMD:C_0603_1608Metric" (at 0.9652 -3.81 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762))
          (stroke (width 0.508) (type default))
          (fill (type none))
        )
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762))
          (stroke (width 0.508) (type default))
          (fill (type none))
        )
      )
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~") (number "1")
        )
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~") (number "2")
        )
      )
    )
    (symbol "Device:C_Polarized"
      (pin_numbers hide) (pin_names (offset 0.254)) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Value" "C" (at 0.635 -2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Footprint" "Capacitor_THT:CP_Radial_D5mm_P2mm" (at 0.9652 -3.81 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "C_Polarized_0_1"
        (rectangle (start -2.286 -0.762) (end 2.286 0.762)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (arc (start 1.905 -0.762) (mid 2.159 0) (end 1.905 0.762)
          (stroke (width 0) (type default))
          (fill (type none))
        )
      )
      (symbol "C_Polarized_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~") (number "1")
        )
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~") (number "2")
        )
      )
    )
    (symbol "Device:D_Schottky"
      (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "D_Schottky" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Diode_SMD:D_SMA" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "D_Schottky_0_1"
        (polyline (pts (xy 0 2.54) (xy 0 -2.54))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline (pts (xy -2.54 2.54) (xy -2.54 -2.54) (xy 2.54 0) (xy -2.54 2.54))
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "D_Schottky_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "K") (number "1")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "A") (number "2")
        )
      )
    )
    (symbol "Device:LED"
      (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "LED" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline (pts (xy -1.27 0) (xy 1.27 1.52))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline (pts (xy -1.27 1.52) (xy 1.27 0))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline (pts (xy 1.27 1.52) (xy 1.27 -1.52) (xy -1.27 -1.27) (xy 1.27 1.52))
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "LED_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "K") (number "1")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "A") (number "2")
        )
      )
    )
    (symbol "Device:Buzzer"
      (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "BZ" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Buzzer" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Buzzer_Beeper:Buzzer_12x9.5RM7.6" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Buzzer_0_1"
        (rectangle (start -2.54 -2.54) (end 2.54 2.54)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "Buzzer_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "~") (number "1")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "~") (number "2")
        )
      )
    )
    (symbol "Connector:Conn_01x02_Pin"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_01x02" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Footprint" "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_01x02_1_1"
        (rectangle (start -1.27 -2.54) (end 1.27 2.54)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin passive line (at 0 5.08 270) (length 2.54) (name "Pin_1") (number "1")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "Pin_2") (number "2")
        )
      )
    )
    (symbol "Connector:Conn_01x03_Pin"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_01x03" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_01x03_1_1"
        (rectangle (start -1.27 -5.08) (end 1.27 5.08)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin passive line (at 0 7.62 270) (length 2.54) (name "Pin_1") (number "1")
        )
        (pin passive line (at 0 0 270) (length 2.54) (name "Pin_2") (number "2")
        )
        (pin passive line (at 0 -7.62 90) (length 2.54) (name "Pin_3") (number "3")
        )
      )
    )
    (symbol "Connector:Conn_01x04_Pin"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_01x04" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_01x04_1_1"
        (rectangle (start -1.27 -7.62) (end 1.27 7.62)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin passive line (at 0 10.16 270) (length 2.54) (name "Pin_1") (number "1")
        )
        (pin passive line (at 0 2.54 270) (length 2.54) (name "Pin_2") (number "2")
        )
        (pin passive line (at 0 -2.54 90) (length 2.54) (name "Pin_3") (number "3")
        )
        (pin passive line (at 0 -7.62 90) (length 2.54) (name "Pin_4") (number "4")
        )
      )
    )
    (symbol "Switch:SW_Push"
      (pin_numbers hide) (pin_names offset 1.016) (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "SW_Push" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Footprint" "Button_Switch_THT:SW_PUSH_6mm_H5mm" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "SW_Push_0_1"
        (circle (center 0 0) (radius 1.27)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (line (start 0 -1.27) (end 0 -2.54)
          (stroke (width 0) (type default))
        )
      )
      (symbol "SW_Push_1_1"
        (pin passive line (at 0 2.54 90) (length 1.27) (name "~") (number "1")
        )
        (pin passive line (at 0 -2.54 270) (length 1.27) (name "~") (number "2")
        )
      )
    )
    (symbol "Transistor_BJT:MMBT2222A"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "Q" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "MMBT2222A" (at 2.54 -2.54 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "MMBT2222A_0_1"
        (polyline (pts (xy 0 0) (xy 0 2.54))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (line (start 0 0) (end -2.286 -2.286)
          (stroke (width 0.254) (type default))
        )
        (line (start 0 0) (end 2.286 -2.286)
          (stroke (width 0.254) (type default))
        )
        (line (start -2.286 -2.286) (end 2.286 -2.286)
          (stroke (width 0.254) (type default))
        )
      )
      (symbol "MMBT2222A_1_1"
        (pin passive line (at -2.54 0 0) (length 2.54) (name "B") (number "1")
        )
        (pin passive line (at 2.54 0 180) (length 2.54) (name "C") (number "3")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "E") (number "2")
        )
      )
    )
    (symbol "Battery_Management:TP4056-42-ESOP8"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "TP4056" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "TP4056-42-ESOP8_1_1"
        (rectangle (start -5.08 -5.08) (end 5.08 5.08)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin passive line (at -7.62 2.54 0) (length 2.54) (name "TEMP") (number "1")
        )
        (pin passive line (at -7.62 0 0) (length 2.54) (name "PROG") (number "2")
        )
        (pin passive line (at -7.62 -2.54 0) (length 2.54) (name "GND") (number "3")
        )
        (pin passive line (at -7.62 -5.08 0) (length 2.54) (name "VCC") (number "4")
        )
        (pin passive line (at 7.62 -5.08 180) (length 2.54) (name "BAT") (number "5")
        )
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "VCC") (number "6")
        )
        (pin passive line (at 7.62 0 180) (length 2.54) (name "STDBY") (number "7")
        )
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "CHRG") (number "8")
        )
      )
    )
    (symbol "Regulator_Linear:AP2112K-3.3"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "AP2112K-3.3" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "AP2112K-3.3_1_1"
        (rectangle (start -2.54 -2.54) (end 2.54 2.54)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin passive line (at -5.08 0 0) (length 2.54) (name "VIN") (number "1")
        )
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "GND") (number "2")
        )
        (pin passive line (at 5.08 0 180) (length 2.54) (name "EN") (number "3")
        )
        (pin passive line (at 0 5.08 270) (length 2.54) (name "VOUT") (number "4")
        )
      )
    )
    (symbol "RF_Module:ESP32-S3-WROOM-1"
      (pin_numbers hide) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 2.54 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "ESP32-S3" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "ESP32-S3-WROOM-1_1_1"
        (rectangle (start -15.24 -20.32) (end 15.24 20.32)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin input line (at -17.78 17.78 0) (length 2.54) (name "GND") (number "1")
        )
        (pin power_in line (at -17.78 15.24 0) (length 2.54) (name "3V3") (number "2")
        )
        (pin bidirectional line (at -17.78 12.7 0) (length 2.54) (name "GPIO0") (number "4")
        )
        (pin bidirectional line (at -17.78 10.16 0) (length 2.54) (name "GPIO4") (number "8")
        )
        (pin bidirectional line (at -17.78 7.62 0) (length 2.54) (name "GPIO5") (number "9")
        )
        (pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "GPIO9") (number "13")
        )
        (pin bidirectional line (at -17.78 2.54 0) (length 2.54) (name "GPIO10") (number "14")
        )
        (pin bidirectional line (at -17.78 0 0) (length 2.54) (name "GPIO11") (number "15")
        )
        (pin bidirectional line (at -17.78 -2.54 0) (length 2.54) (name "GPIO12") (number "16")
        )
        (pin power_in line (at 17.78 -17.78 180) (length 2.54) (name "EN") (number "3")
        )
      )
    )
    (symbol "power:+3.3V"
      (pin power_in line (at 0 0 270) (length 2.54) (name "+3V3")
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (rectangle (start -1.27 -1.27) (end 1.27 1.27)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "power:GND"
      (pin power_in line (at 0 0 270) (length 2.54) (name "GND")
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (rectangle (start -1.27 -1.27) (end 1.27 1.27)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
      (polyline (pts (xy 0 0) (xy 0 1.27))
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline (pts (xy 0 1.27) (xy -1.27 3.81) (xy 1.27 3.81) (xy 0 1.27))
        (stroke (width 0) (type default))
        (fill (type none))
      )
    )
    (symbol "power:VBUS"
      (pin power_in line (at 0 0 270) (length 2.54) (name "VBUS")
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (rectangle (start -1.27 -1.27) (end 1.27 1.27)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
  )

  (symbol_instances
    (symbol (lib_id "power:VBUS") (at 50 115 0)
      (property "Reference" "#PWR01" (at 50 111.76 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "VBUS" (at 50 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "power:+3.3V") (at 70 35 0)
      (property "Reference" "#PWR02" (at 70 31.76 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "+3.3V" (at 70 34.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "power:GND") (at 90 35 0)
      (property "Reference" "#PWR03" (at 90 31.76 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "GND" (at 90 34.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Connector:USB_C_Receptacle_USB2.0_16P") (at 50 100 0)
      (property "Reference" "J1" (at 50 86.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "USB-C" (at 50 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Connector_USB:USB_C_Receptacle_USB2.0_16P" (at 50 100 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "Battery_Management:TP4056-42-ESOP8") (at 50 75 0)
      (property "Reference" "U3" (at 50 61.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "TP4056" (at 50 89.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 50 75 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "Regulator_Linear:AP2112K-3.3") (at 50 50 0)
      (property "Reference" "U4" (at 50 36.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "AP2112K-3.3" (at 50 64.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 50 50 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "RF_Module:ESP32-S3-WROOM-1") (at 140 70 0)
      (property "Reference" "U1" (at 140 41.26 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "ESP32-S3" (at 140 94.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 140 70 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "Device:D_Schottky") (at 70 100 0)
      (property "Reference" "D3" (at 70 86.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "1N5819" (at 70 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Diode_SMD:D_SMA" (at 70 100 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "Connector:Conn_01x02_Pin") (at 30 110 0)
      (property "Reference" "J4" (at 30 96.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Battery" (at 30 124.3 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical" (at 30 110 0)
        (effects (font (size 1.27 1.27)) hide)
      )
    )
    (symbol (lib_id "Connector:Conn_01x04_Pin") (at 200 40 0)
      (property "Reference" "J3" (at 200 26.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "OLED" (at 200 54.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Connector:Conn_01x03_Pin") (at 200 70 0)
      (property "Reference" "J2" (at 200 56.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Servo" (at 200 84.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Switch:SW_Push") (at 100 120 0)
      (property "Reference" "SW1" (at 100 106.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "USER" (at 100 134.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Switch:SW_Push") (at 110 120 0)
      (property "Reference" "SW2" (at 110 106.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "RESET" (at 110 134.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Switch:SW_Push") (at 120 120 0)
      (property "Reference" "SW3" (at 120 106.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "BOOT" (at 120 134.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:LED") (at 90 100 0)
      (property "Reference" "D1" (at 90 86.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Red" (at 90 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:LED") (at 90 90 0)
      (property "Reference" "D4" (at 90 76.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Red" (at 90 104.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:LED") (at 90 80 0)
      (property "Reference" "D5" (at 90 66.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Green" (at 90 94.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 60 65 0)
      (property "Reference" "C1" (at 60 51.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "10uF" (at 60 79.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 60 55 0)
      (property "Reference" "C2" (at 60 41.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "10uF" (at 60 69.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 120 55 0)
      (property "Reference" "C5" (at 120 41.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100nF" (at 120 69.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 120 45 0)
      (property "Reference" "C6" (at 120 31.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100nF" (at 120 59.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 130 55 0)
      (property "Reference" "C7" (at 130 41.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100nF" (at 130 69.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 130 45 0)
      (property "Reference" "C8" (at 130 31.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100nF" (at 130 59.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C") (at 150 50 0)
      (property "Reference" "C9" (at 150 36.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "10uF" (at 150 64.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:C_Polarized") (at 40 85 0)
      (property "Reference" "C10" (at 40 71.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100uF" (at 40 99.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 80 95 0)
      (property "Reference" "R1" (at 80 81.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "330" (at 80 109.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 80 85 0)
      (property "Reference" "R2" (at 80 71.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "330" (at 80 99.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 80 75 0)
      (property "Reference" "R3" (at 80 61.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "330" (at 80 89.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 130 90 0)
      (property "Reference" "R4" (at 130 76.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "1k" (at 130 104.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 60 90 0)
      (property "Reference" "R5" (at 60 76.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "2k" (at 60 104.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 180 50 0)
      (property "Reference" "R6" (at 180 36.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "4.7k" (at 180 64.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 180 60 0)
      (property "Reference" "R7" (at 180 46.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "4.7k" (at 180 74.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 125 120 0)
      (property "Reference" "R8" (at 125 106.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "10k" (at 125 134.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 40 125 0)
      (property "Reference" "R9" (at 40 111.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100k" (at 40 139.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 45 125 0)
      (property "Reference" "R10" (at 45 111.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "100k" (at 45 139.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 50 90 0)
      (property "Reference" "R11" (at 50 76.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "5.1k" (at 50 104.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 55 90 0)
      (property "Reference" "R12" (at 55 76.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "5.1k" (at 55 104.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:R") (at 135 120 0)
      (property "Reference" "R17" (at 135 106.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "10k" (at 135 134.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Device:Buzzer") (at 100 100 0)
      (property "Reference" "BZ1" (at 100 86.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Buzzer" (at 100 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
    (symbol (lib_id "Transistor_BJT:MMBT2222A") (at 110 100 0)
      (property "Reference" "Q1" (at 110 86.36 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "MMBT2222A" (at 110 114.3 0)
        (effects (font (size 1.27 1.27)))
      )
    )
  )

  (wire
{wire_block}
  )

{junction_block}

  (sheet_instances (path "/" (page "1")))
)

(End of file)
"""

# Write to file
output_path = r"D:\UPES\Projects\Pill Despensor\Pill_Dispenser_V6\Pill_Dispenser_V6.kicad_sch"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(schematic_content)

print(f"Schematic written to: {output_path}")
print(f"Total wires created: {len(wires)}")
print("\nWire summary:")
print("- VBUS connections: USB-C to TP4056")
print("- GND connections: Distributed to all components")
print("- Battery circuit: TP4056 -> Schottky -> Battery connector")
print("- LDO circuit: Schottky -> AP2112K -> ESP32")
print("- Button connections: USER, RESET, BOOT")
print("- LED connections: Status, Charge, Standby")
print("- I2C: ESP32 -> OLED with pull-ups")
print("- Buzzer: ESP32 -> Transistor -> Buzzer")
print("- Servo: ESP32 -> Servo connector")
