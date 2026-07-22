import re
import sys

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see if we can find the block for D2 or USBLC6 components
import re

# Match the entire symbol definition block for D2 or USBLC6
# Typically: (symbol (lib_id "Power_Protection:USBLC6-2SC6") ... ))
# And also the reference symbol in the sheet: (symbol (lib_id "Power_Protection:USBLC6-2SC6")... )
print("Before removal length:", len(content))

content = re.sub(r'\(symbol \(lib_id "Power_Protection:USBLC6-2SC6"\).*?\(property "Datasheet".*?\)\)\)\)', '', content, flags=re.DOTALL)
content = re.sub(r'\(symbol \(lib_id "Power_Protection:USBLC6-2P6"\).*?\(property "Datasheet".*?\)\)\)\)', '', content, flags=re.DOTALL)

# Delete D2 instance
content = re.sub(r'\(symbol\s*\(lib_id "Power_Protection:USBLC6-2SC6"\).*?\(uuid "[^"]+"(?:\)\s*|\s*)\)', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("After removal length:", len(content))
