box_file = "page_001 copy.box"
old_txt_file = "page_001 copy.txt"      
corrected_txt_file = "page_001.gt.txt"  

with open(box_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

box_chars = [line.split()[0] for line in lines if line.strip()]

with open(old_txt_file, "r", encoding="utf-8") as f:
    old_lines = f.readlines()

corrected_lines = []
box_index = 0 

for line_num, line in enumerate(old_lines):
    corrected_line = ""

    for char in line:
        if char.isspace():
            corrected_line += char 
        else:
            if box_index < len(box_chars):
                corrected_line += box_chars[box_index]
                box_index += 1
            else:
                print(f"Ran out of box characters at line {line_num+1}, char: '{char}'")
                corrected_line += char 

    corrected_lines.append(corrected_line)

with open(corrected_txt_file, "w", encoding="utf-8") as f:
    f.writelines(corrected_lines)

print(f"\nDone! Saved corrected text to: {corrected_txt_file}")
print(f"Characters used: {box_index}/{len(box_chars)}")
