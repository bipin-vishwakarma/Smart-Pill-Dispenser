import os

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace USBLC6-2SC6 with the standard USBLC6-4SC6 or something valid
# Actually, the error complains about extended symbol USBLC6-2P6.
content = content.replace('(lib_id "Power_Protection:USBLC6-2SC6")', '(lib_id "Power_Protection:USBLC6-2SC6")')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
