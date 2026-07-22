import os
import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the offending symbol
target = '(symbol "Power_Protection:USBLC6-2SC6" (extends "USBLC6-2P6")'

# We'll just replace the (extends "USBLC6-2P6") with something harmless or drop this whole symbol.
# Since it's causing an error, let's just drop the extends statement.
if '(extends "USBLC6-2P6")' in content:
    content = content.replace('(extends "USBLC6-2P6")', '')
    print("Removed extends clause")
else:
    print("did not find extends clause")

content = content.replace('USBLC6-2P6', 'DummyName')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fix applied")
