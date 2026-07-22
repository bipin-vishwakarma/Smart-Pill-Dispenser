#!/usr/bin/env python3
"""
Generate clean Pill Dispenser V6 KiCad schematic with proper wire format.
"""

def gen_schematic():
    # Wire definitions with proper coordinates
    wires = [
        # VBUS - USB to TP4056
        {'pts': [(39.84, 102.54), (60.16, 102.54)], 'uuid': 'w0001'},
        {'pts': [(39.84, 102.54), (42.38, 69.92)], 'uuid': 'w0002'},
        {'pts': [(42.38, 69.92), (57.62, 72.46)], 'uuid': 'w0003'},
        # GND - USB to TP4056
        {'pts': [(39.84, 100), (60.16, 100)], 'uuid': 'w0004'},
        {'pts': [(39.84, 100), (42.38, 72.46)], 'uuid': 'w0005'},
        # TP4056 GND to LDO GND
        {'pts': [(42.38, 72.46), (50, 44.92)], 'uuid': 'w0006'},
        # LDO input from Schottky
        {'pts': [(70, 94.92), (44.92, 50)], 'uuid': 'w0007'},
        # LDO output to ESP32
        {'pts': [(50, 55.08), (122.22, 85.24)], 'uuid': 'w0008'},
        # Battery path
        {'pts': [(57.62, 69.92), (70, 105.08)], 'uuid': 'w0009'},
        {'pts': [(70, 105.08), (30, 115.08)], 'uuid': 'w0010'},
    ]
    
    # Build wire S-expressions
    wire_block = []
    for w in wires:
        x1, y1 = w['pts'][0]
        x2, y2 = w['pts'][1]
        wire_block.append(f'    (wire (pts (xy {x1} {y1}) (xy {x2} {y2})) (uuid "{w["uuid"]}"))')
    
    wires_str = '\n'.join(wire_block)
    
    schematic = f'''(kicad_sch (version 20211117) (generator "Pill_Dispenser_V6")

  (uuid "a1b05787-cd6a-483e-afe0-48eda7657ffa")

  (paper "A4")

  (lib_symbols
    (symbol "power:+3.3V"
      (pin power_in line (at 0 0 270) (length 2.54) (name "+3V3") (number "1"))
      (rectangle (start -1.27 -1.27) (end 1.27 1.27) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "power:GND"
      (pin power_in line (at 0 0 270) (length 2.54) (name "GND") (number "1"))
      (rectangle (start -1.27 -1.27) (end 1.27 1.27) (stroke (width 0.254) (type default)) (fill (type background)))
      (polyline (pts (xy 0 0) (xy 0 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      (polyline (pts (xy 0 1.27) (xy -1.27 3.81) (xy 1.27 3.81) (xy 0 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "power:VBUS"
      (pin power_in line (at 0 0 270) (length 2.54) (name "VBUS") (number "1"))
      (rectangle (start -1.27 -1.27) (end 1.27 1.27) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "Device:R"
      (pin_numbers hide)
      (pin_names (offset 0))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Resistor_SMD:R_0603_1608Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~") (number "1"))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~") (number "2"))
      )
    )
    (symbol "Device:C"
      (pin_numbers hide)
      (pin_names (offset 0.254))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
      )
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.54) (name "~") (number "1"))
        (pin passive line (at 0 -3.81 90) (length 2.54) (name "~") (number "2"))
      )
    )
    (symbol "Device:LED"
      (pin_numbers hide)
      (pin_names (offset 0))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "D" (at 2.54 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "LED" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 1.52)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 1.52) (xy 1.27 0)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.52) (xy 1.27 -1.52) (xy -1.27 -1.27) (xy 1.27 1.52)) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "LED_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "K") (number "1"))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "A") (number "2"))
      )
    )
    (symbol "Device:D_Schottky"
      (pin_numbers hide)
      (pin_names (offset 0))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "D" (at 2.54 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "D_Schottky" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (symbol "D_Schottky_0_1"
        (polyline (pts (xy 0 2.54) (xy 0 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 2.54) (xy -2.54 -2.54) (xy 2.54 0) (xy -2.54 2.54)) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "D_Schottky_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "K") (number "1"))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "A") (number "2"))
      )
    )
    (symbol "Battery_Management:TP4056"
      (pin_numbers hide)
      (pin_names (offset 1.016))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "U" (at 2.54 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "TP4056" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (symbol "TP4056_1_1"
        (rectangle (start -5.08 -5.08) (end 5.08 5.08) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -7.62 2.54 0) (length 2.54) (name "TEMP") (number "1"))
        (pin passive line (at -7.62 0 0) (length 2.54) (name "PROG") (number "2"))
        (pin passive line (at -7.62 -2.54 0) (length 2.54) (name "GND") (number "3"))
        (pin passive line (at -7.62 -5.08 0) (length 2.54) (name "VCC") (number "4"))
        (pin passive line (at 7.62 -5.08 180) (length 2.54) (name "BAT") (number "5"))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "VCC") (number "6"))
        (pin passive line (at 7.62 0 180) (length 2.54) (name "STBY") (number "7"))
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "CHRG") (number "8"))
      )
    )
    (symbol "Regulator_Linear:AP2112K-3.3"
      (pin_numbers hide)
      (pin_names (offset 1.016))
      (in_bom yes)
      (on_board yes)
      (property "Reference" "U" (at 2.54 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "AP2112K-3.3" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (symbol "AP2112K-3.3_1_1"
        (rectangle (start -2.54 -2.54) (end 2.54 2.54) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -5.08 0 0) (length 2.54) (name "VIN") (number "1"))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "GND") (number "2"))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "EN") (number "3"))
        (pin passive line (at 0 5.08 270) (length 2.54) (name "VOUT") (number "4"))
      )
    )
    (symbol "Connector:USB_C_Receptacle_USB2.0_16P"
      (pin passive line (at -10.16 0 0) (length 2.54) (name "GND") (number "A6"))
      (pin passive line (at -10.16 2.54 0) (length 2.54) (name "VBUS") (number "A1"))
      (pin passive line (at -10.16 5.08 0) (length 2.54) (name "CC1") (number "A5"))
      (pin passive line (at -10.16 7.62 0) (length 2.54) (name "D+") (number "A4"))
      (pin passive line (at -10.16 10.16 0) (length 2.54) (name "D-") (number "A7"))
      (pin passive line (at -10.16 12.7 0) (length 2.54) (name "CC2") (number "B5"))
      (pin passive line (at 10.16 0 180) (length 2.54) (name "GND") (number "B6"))
      (pin passive line (at 10.16 2.54 180) (length 2.54) (name "VBUS") (number "B1"))
      (rectangle (start -10.16 -2.54) (end 10.16 15.24) (stroke (width 0.254) (type default)) (fill (type background)))
    )
  )

  (symbol_instances
    (symbol (lib_id "power:VBUS") (at 50 115 0)
      (property "Reference" "#PWR01" (at 50 111.76 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "VBUS" (at 50 114.3 0) (effects (font (size 1.27 1.27))))
    )
    (symbol (lib_id "power:+3.3V") (at 70 35 0)
      (property "Reference" "#PWR02" (at 70 31.76 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+3.3V" (at 70 34.3 0) (effects (font (size 1.27 1.27))))
    )
    (symbol (lib_id "power:GND") (at 90 35 0)
      (property "Reference" "#PWR03" (at 90 31.76 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 90 34.3 0) (effects (font (size 1.27 1.27))))
    )
    (symbol (lib_id "Connector:USB_C_Receptacle_USB2.0_16P") (at 50 100 0)
      (property "Reference" "J1" (at 50 86.36 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB-C" (at 50 114.3 0) (effects (font (size 1.27 1.27))))
    )
    (symbol (lib_id "Battery_Management:TP4056") (at 50 75 0)
      (property "Reference" "U3" (at 50 61.36 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TP4056" (at 50 89.3 0) (effects (font (size 1.27 1.27))))
    )
    (symbol (lib_id "Regulator_Linear:AP2112K-3.3") (at 50 50 0)
      (property "Reference" "U4" (at 50 36.36 0) (effects (font (size 1.27 1.27))))
      (property "Value" "AP2112K-3.3" (at 50 64.3 0) (effects (font (size 1.27 1.27))))
    )
  )

  (wire
{wires_str}
  )

  (junction (at 39.84 102.54) (diameter 0.8) (color 0 0 0 0))
  (junction (at 39.84 100) (diameter 0.8) (color 0 0 0 0))
  (junction (at 42.38 72.46) (diameter 0.8) (color 0 0 0 0))
  (junction (at 50 55.08) (diameter 0.8) (color 0 0 0 0))
  (junction (at 70 105.08) (diameter 0.8) (color 0 0 0 0))

  (sheet_instances (path "/" (page "1")))
)
'''
    return schematic

# Generate and save
content = gen_schematic()

# Verify balance
opens = content.count('(')
closes = content.count(')')
print(f'Parens: opens={opens}, closes={closes}, balanced={opens==closes}')

with open(r'D:\UPES\Projects\Pill Despensor\Pill_Dispenser_V6\Pill_Dispenser_V6.kicad_sch', 'w') as f:
    f.write(content)

print('Schematic saved!')
print(f'Total wires: 10')
