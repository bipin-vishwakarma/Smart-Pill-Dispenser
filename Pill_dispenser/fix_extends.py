import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Strategy: Replace the AP2112K-3.3 extends block with a full copy of AP2204K-1.5
# and the MMBT2222A extends block with a full copy of Q_NPN_BEC
# but with updated properties (Reference, Value, Footprint, Datasheet, Description)

# Helper: find a (symbol "name" ...) block by counting parens
def find_symbol_block(text, name):
    target = f'(symbol "{name}"'
    idx = text.find(target)
    if idx == -1:
        return None, -1, -1
    count = 0
    for i in range(idx, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count == 0:
            return text[idx:i+1], idx, i+1
    return None, -1, -1

# 1. Fix AP2112K-3.3: Remove the extends block and keep the parent AP2204K-1.5
#    since U4 actually uses lib_id "Regulator_Linear:AP2112K-3.3"
#    We need to keep the parent definition AND fix the child.
#
#    Actually, the simplest fix is to just remove the extends clause
#    and make AP2112K-3.3 self-contained by copying sub-symbols from AP2204K-1.5

# Find the AP2204K-1.5 parent block
parent_block, _, _ = find_symbol_block(text, "Regulator_Linear:AP2204K-1.5")
if parent_block:
    print("Found AP2204K-1.5 parent block, length:", len(parent_block))
else:
    print("AP2204K-1.5 NOT FOUND!")

# Find the AP2112K-3.3 extends block  
child_block, child_start, child_end = find_symbol_block(text, "Regulator_Linear:AP2112K-3.3")
if child_block:
    print("Found AP2112K-3.3 child block, length:", len(child_block))
    
    # Extract sub-symbols from parent (the graphical and pin definitions)
    # These are (symbol "AP2204K-1.5_0_1" ...) and (symbol "AP2204K-1.5_1_1" ...) 
    parent_subsymbols = re.findall(r'\(symbol "AP2204K-1\.5_\d+_\d+"[^)]*\)(?:[^(]*\([^)]*\))*[^)]*\)', parent_block)
    
    # Actually, let's just extract them properly with paren counting
    sub_blocks = []
    search_text = parent_block
    for match in re.finditer(r'\(symbol "AP2204K-1\.5_', search_text):
        start = match.start()
        count = 0
        for i in range(start, len(search_text)):
            if search_text[i] == '(':
                count += 1
            elif search_text[i] == ')':
                count -= 1
            if count == 0:
                sub_block = search_text[start:i+1]
                # Rename to AP2112K-3.3
                sub_block = sub_block.replace('AP2204K-1.5_', 'AP2112K-3.3_')
                sub_blocks.append(sub_block)
                break
    
    print(f"Found {len(sub_blocks)} sub-symbol blocks from parent")
    
    # Build new AP2112K-3.3 block: keep its properties but add sub-symbols
    # Remove the (extends "AP2204K-1.5") part
    new_child = child_block.replace('(extends "AP2204K-1.5") ', '')
    
    # Insert sub-symbols before the closing paren
    # The child block ends with )) - we need to insert before the last )
    insert_pos = len(new_child) - 1  # before last )
    sub_text = ' '.join(sub_blocks)
    new_child = new_child[:insert_pos] + ' ' + sub_text + new_child[insert_pos:]
    
    text = text[:child_start] + new_child + text[child_end:]
    print("Replaced AP2112K-3.3 block")
else:
    print("AP2112K-3.3 NOT FOUND!")

# 2. Fix MMBT2222A: same approach
parent_block2, _, _ = find_symbol_block(text, "Transistor_BJT:Q_NPN_BEC")
if parent_block2:
    print("Found Q_NPN_BEC parent block, length:", len(parent_block2))
else:
    print("Q_NPN_BEC NOT FOUND!")

child_block2, child_start2, child_end2 = find_symbol_block(text, "Transistor_BJT:MMBT2222A")
if child_block2:
    print("Found MMBT2222A child block, length:", len(child_block2))
    
    sub_blocks2 = []
    for match in re.finditer(r'\(symbol "Q_NPN_BEC_', parent_block2):
        start = match.start()
        count = 0
        for i in range(start, len(parent_block2)):
            if parent_block2[i] == '(':
                count += 1
            elif parent_block2[i] == ')':
                count -= 1
            if count == 0:
                sub_block = parent_block2[start:i+1]
                sub_block = sub_block.replace('Q_NPN_BEC_', 'MMBT2222A_')
                sub_blocks2.append(sub_block)
                break
    
    print(f"Found {len(sub_blocks2)} sub-symbol blocks from Q_NPN_BEC parent")
    
    new_child2 = child_block2.replace('(extends "Q_NPN_BEC") ', '')
    insert_pos2 = len(new_child2) - 1
    sub_text2 = ' '.join(sub_blocks2)
    new_child2 = new_child2[:insert_pos2] + ' ' + sub_text2 + new_child2[insert_pos2:]
    
    text = text[:child_start2] + new_child2 + text[child_end2:]
    print("Replaced MMBT2222A block")
else:
    print("MMBT2222A NOT FOUND!")

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

# Verify
count = 0
for c in text:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
print("Final parenthesis balance:", count)
print("Final file size:", len(text))
print("Remaining extends:", re.findall(r'\(extends\s+"([^"]+)"\)', text))
