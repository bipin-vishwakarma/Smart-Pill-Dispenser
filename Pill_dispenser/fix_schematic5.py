import sys
import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

new_text = ''
i = 0
changed = False
while i < len(text):
    idx = text.find('(symbol "', i)
    if idx == -1:
        new_text += text[i:]
        break
        
    new_text += text[i:idx]
    
    count = 0
    end_idx = -1
    for p in range(idx, len(text)):
        if text[p] == '(': count += 1
        elif text[p] == ')': count -= 1
        if count == 0:
            end_idx = p + 1
            break
            
    if end_idx != -1:
        block = text[idx:end_idx]
        
        if '(extends ' in block and not '(uuid ' in block:
            parent_match = re.search(r'\(extends\s+"([^"]+)"\)', block)
            if parent_match:
                parent = parent_match.group(1)
                parent_def = f'(symbol "{parent}"'
                if parent_def not in text:
                    print(f'Removing broken library symbol: {block[:50]}... extending {parent}')
                    changed = True
                    i = end_idx
                    continue
        
        new_text += block
        i = end_idx
    else:
        new_text += text[i:]
        break

if changed:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Cleaned up broken extended symbols')
else:
    print('No broken extended symbols found')
