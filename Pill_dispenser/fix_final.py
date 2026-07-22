import re

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

print("Before:", len(text))

# Find and remove the DummyName symbol block using parenthesis balancing
target = '(symbol "Power_Protection:DummyName"'
idx = text.find(target)

if idx != -1:
    count = 0
    end_idx = -1
    for i in range(idx, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count == 0:
            end_idx = i + 1
            break
    
    if end_idx != -1:
        # Remove the block and any trailing whitespace
        text = text[:idx] + text[end_idx:]
        print(f"Removed DummyName block: {end_idx - idx} chars")
    else:
        print("ERROR: Could not find end of DummyName block")
else:
    print("DummyName block not found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("After:", len(text))

# Verify parenthesis balance
count = 0
for c in text:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
print("Parenthesis balance:", count)
