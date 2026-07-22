import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Define footprint mapping based on requirements
footprint_mapping = {
    # Microcontroller
    r'(property "Value" ".*ESP32-S3.*")': 'RF_Module:ESP32-S3-MINI-1',
    # Voltage Regulator
    r'(property "Value" "AP2112K-3.3")': 'Package_TO_SOT_SMD:SOT-23-5',
    # Connectors
    r'(property "Value" "USB_C_Receptacle_USB2.0")': 'Connector_USB:USB_C_Receptacle_USB2.0_16P',
    r'(property "Value" "Conn_01x02")': 'Connector_JST:JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal',
    r'(property "Value" "Conn_01x03")': 'Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal',
    r'(property "Value" "Conn_01x04")': 'Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Horizontal',
    # Discrete
    r'(property "Value" "MMBT2222A")': 'Package_TO_SOT_SMD:SOT-23',
    r'(property "Value" "SW_Push")': 'Button_Switch_SMD:SW_SPST_B3U-1000P',
    r'(property "Value" "Buzzer")': 'Buzzer_Beeper:Buzzer_12x9.5RM7.6',
    r'(property "Value" "LED")': 'LED_SMD:LED_0603_1608Metric',
    # Resistors
    r'(property "Value" "\d+k?"\)|\(property "Value" "\d+R?"\))': 'Resistor_SMD:R_0603_1608Metric',
    r'(property "Value" "10k")': 'Resistor_SMD:R_0603_1608Metric',
    r'(property "Value" "5.1k")': 'Resistor_SMD:R_0603_1608Metric',
    r'(property "Value" "1k")': 'Resistor_SMD:R_0603_1608Metric',
    r'(property "Value" "220")': 'Resistor_SMD:R_0603_1608Metric',
}

# The above mapping might be too broad or problematic. Let's do it by reference or exact value.
# Let's extract all components first.
import sys

components = []
# Match symbols placed in the schematic, format is (symbol (lib_id ...) (at ...) ... (property "Reference" "U1" ... ) (property "Value" "ESP32..." ... ))
# We can find all instances of (symbol (lib_id ...) ...)
symbol_instances_match = re.finditer(r'\(symbol\s+\(lib_id "(.*?)"\)\s+\(at ([\d\.\-]+) ([\d\.\-]+)[^\)]*\)\s+\(unit \d+\)\s+\(exclude_from_sim no\)\s+\(in_bom yes\)\s+\(on_board yes\)\s+\(dnp no\)\s+\(fields_autoplaced yes\)\s+\(uuid [^\)]+\)\s+\(property "Reference" "([^"]+)"[^\)]+\).*?\(property "Value" "([^"]+)"', text, re.DOTALL)

for match in symbol_instances_match:
    components.append({
        'lib_id': match.group(1),
        'ref': match.group(4),
        'value': match.group(5),
    })

print("Components found:", len(components))
for c in components:
    print(c)

