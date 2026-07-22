import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# We need a proper paren-matching scanner to find symbol instances.
# A symbol instance starts with '(symbol (lib_id' and is outside the '(lib_symbols' block.
instances = []
idx = 0
lib_symbols_idx = text.find('(lib_symbols')
if lib_symbols_idx != -1:
    # Skip past the lib_symbols block
    count = 0
    for i in range(lib_symbols_idx, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count == 0:
            idx = i + 1
            break

while True:
    start_idx = text.find('(symbol (lib_id', idx)
    if start_idx == -1:
        break
        
    count = 0
    end_idx = -1
    for i in range(start_idx, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count == 0:
            end_idx = i + 1
            break
            
    if end_idx != -1:
        instances.append(text[start_idx:end_idx])
        idx = end_idx
    else:
        break

print(f"Found {len(instances)} component instances.")

missing_fp = 0
for inst in instances:
    ref_match = re.search(r'\(property "Reference" "([^"]+)"', inst)
    val_match = re.search(r'\(property "Value" "([^"]+)"', inst)
    fp_match = re.search(r'\(property "Footprint" "([^"]*)"', inst)
    
    ref = ref_match.group(1) if ref_match else "?"
    val = val_match.group(1) if val_match else "?"
    fp = fp_match.group(1) if fp_match else ""
    
    if not fp:
        missing_fp += 1
        print(f"[{ref}] ({val}) -> NO FOOTPRINT")
    else:
        print(f"[{ref}] ({val}) -> {fp}")

print(f"\nComponents missing footprints: {missing_fp}")
