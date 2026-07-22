import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Check if there are any remaining issues
# 1. Check for any "extends" references to non-existent symbols
extends_refs = re.findall(r'\(extends\s+"([^"]+)"\)', text)
print("Extends references:", extends_refs)

# 2. Check for the symbols these extend
for parent in extends_refs:
    parent_pattern = f'(symbol "{parent}"'
    if parent_pattern in text:
        print(f"  Parent '{parent}' FOUND in file")
    else:
        print(f"  Parent '{parent}' MISSING - this is the problem!")

# 3. Check for any remaining DummyName or USBLC references
print("DummyName count:", text.count('DummyName'))
print("USBLC count:", text.count('USBLC'))

# 4. Look for any empty space between closing parens of lib_symbols and first symbol instance
# The file structure should be:
# (kicad_sch ... (lib_symbols (symbol ...) (symbol ...)) (symbol (lib_id ...) ...) ...)
# Let's check the transition from lib_symbols to first symbol instance
print("embedded_fonts count:", text.count('embedded_fonts'))

# 5. Let's also check if the file starts/ends correctly
print("Starts with:", text[:30])
print("Ends with:", text[-30:])
