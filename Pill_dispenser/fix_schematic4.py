import sys

filepath = 'd:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\Pill_Dispenser_V2.kicad_sch'

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # The block we want to remove is the standard library symbol definition:
    # (symbol "Power_Protection:USBLC6-2SC6" ... )
    # Let's find it.
    prefix = '(symbol "Power_Protection:USBLC6-2SC6"'
    idx = text.find(prefix)
    
    if idx != -1:
        count = 0
        end_idx = -1
        # Parse the s-expression
        for i in range(idx, len(text)):
            if text[i] == '(': 
                count += 1
            elif text[i] == ')': 
                count -= 1
            
            if count == 0:
                end_idx = i + 1
                break
                
        if end_idx != -1:
            # We found the whole block! Remove it.
            # Also clean up any leading/trailing whitespace
            text = text[:idx] + text[end_idx:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            print("SUCCESS: Symbol block completely removed. Characters removed:", end_idx - idx)
        else:
            print("ERROR: Unbalanced parentheses in symbol block")
    else:
        print("Symbol block not found")
        
except Exception as e:
    print("Exception:", str(e))
