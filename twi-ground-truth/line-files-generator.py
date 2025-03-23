# # import os
# # from PIL import Image

# # # === CONFIG ===
# # base_name = "page_001"
# # box_file = f"{base_name}.box"
# # image_file = f"{base_name}.tif"
# # gt_file = f"{base_name}.gt.txt"
# # output_dir = f"{base_name}_lines"
# # os.makedirs(output_dir, exist_ok=True)

# # # --- Load image ---
# # image = Image.open(image_file)

# # # --- Read box entries ---
# # with open(box_file, "r", encoding="utf-8") as f:
# #     raw_boxes = f.readlines()

# # box_entries = []
# # for line in raw_boxes:
# #     parts = line.strip().split()
# #     if len(parts) == 6:
# #         char, x1, y1, x2, y2, _ = parts
# #         box_entries.append({
# #             "char": char,
# #             "x1": int(x1),
# #             "y1": int(y1),
# #             "x2": int(x2),
# #             "y2": int(y2)
# #         })

# # # --- Read GT lines ---
# # with open(gt_file, "r", encoding="utf-8") as f:
# #     gt_lines = [line.strip() for line in f if line.strip()]

# # # --- Helper function: Match words in box chars ---
# # def find_word_span(box_entries, target_word, start=0):
# #     buffer = ""
# #     for i in range(start, len(box_entries)):
# #         buffer += box_entries[i]["char"]
# #         if buffer == target_word:
# #             return i - len(target_word) + 1, i
# #         elif not target_word.startswith(buffer):
# #             # restart the buffer
# #             buffer = ""
# #     return None

# # # --- Process each line from GT text ---
# # box_pointer = 0
# # for i, line in enumerate(gt_lines):
# #     print(f"\n🔍 Processing line {i}: {line}")
# #     words = line.split()
# #     if len(words) < 1:
# #         print(f"⚠️ Skipping empty line {i}")
# #         continue

# #     first_word = words[0]
# #     last_word = words[-1]

# #     print(f"➡ First word: '{first_word}', Last word: '{last_word}'")

# #     # Find start of line (first word)
# #     start_span = find_word_span(box_entries, first_word, box_pointer)
# #     if not start_span:
# #         print(f"❌ Couldn't match first word '{first_word}' in box data.")
# #         continue
# #     start_idx = start_span[0]

# #     # Find end of line (last word), search from end of current line
# #     end_span = find_word_span(box_entries, last_word, start_idx)
# #     if not end_span:
# #         print(f"❌ Couldn't match last word '{last_word}' in box data.")
# #         continue
# #     end_idx = end_span[1]

# #     print(f"✅ Found character indices: {start_idx} to {end_idx}")

# #     line_boxes = box_entries[start_idx:end_idx + 1]

# #     # Compute bounding box
# #     x1 = min(b["x1"] for b in line_boxes)
# #     y1 = min(b["y1"] for b in line_boxes)
# #     x2 = max(b["x2"] for b in line_boxes)
# #     y2 = max(b["y2"] for b in line_boxes)

# #     # Crop image
# #     cropped = image.crop((x1, y1, x2, y2))
# #     line_img_path = os.path.join(output_dir, f"{base_name}-line{i}.tif")
# #     cropped.save(line_img_path)

# #     # Write .gt.txt
# #     gt_path = os.path.join(output_dir, f"{base_name}-line{i}.gt.txt")
# #     with open(gt_path, "w", encoding="utf-8") as f:
# #         f.write(line + "\n")

# #     # Write .box with updated coordinates
# #     box_path = os.path.join(output_dir, f"{base_name}-line{i}.box")
# #     with open(box_path, "w", encoding="utf-8") as f:
# #         for b in line_boxes:
# #             new_x1 = b["x1"] - x1
# #             new_y1 = b["y1"] - y1
# #             new_x2 = b["x2"] - x1
# #             new_y2 = b["y2"] - y1
# #             f.write(f"{b['char']} {new_x1} {new_y1} {new_x2} {new_y2} 0\n")

# #     # Advance box pointer
# #     box_pointer = end_idx + 1
# #     print(f"💾 Saved line {i} as: {base_name}-line{i}.tif/.box/.gt.txt")

# # print(f"\n✅ Done! All lines processed and saved in: {output_dir}/")

# import os
# from PIL import Image

# # === CONFIG ===
# base_name = "page_001"
# box_file = f"{base_name}.box"
# image_file = f"{base_name}.tif"
# gt_file = f"{base_name}.gt.txt"
# output_dir = f"{base_name}_lines"
# horizontal_pad = 5  # width tolerance
# vertical_pad = 5    # height tolerance

# os.makedirs(output_dir, exist_ok=True)

# # --- Load image ---
# image = Image.open(image_file)

# # --- Read box entries ---
# with open(box_file, "r", encoding="utf-8") as f:
#     raw_boxes = f.readlines()

# box_entries = []
# for line in raw_boxes:
#     parts = line.strip().split()
#     if len(parts) == 6:
#         char, x, y, w, h, _ = parts
#         box_entries.append({
#             "char": char,
#             "x": int(x),
#             "y": int(y),
#             "w": int(w),
#             "h": int(h)
#         })

# # --- Read GT lines ---
# with open(gt_file, "r", encoding="utf-8") as f:
#     gt_lines = [line.strip() for line in f if line.strip()]

# # --- Helper: Find first and last word spans in box_entries ---
# def find_word_span(box_entries, target_word, start=0):
#     buffer = ""
#     for i in range(start, len(box_entries)):
#         buffer += box_entries[i]["char"]
#         if buffer == target_word:
#             return i - len(target_word) + 1, i
#         elif not target_word.startswith(buffer):
#             buffer = ""
#     return None

# # --- Process each GT line ---
# box_pointer = 0
# for i, line in enumerate(gt_lines):
#     print(f"\n🔍 Processing line {i}: {line}")
#     words = line.split()
#     if len(words) < 1:
#         print(f"⚠️ Skipping empty line {i}")
#         continue

#     first_word = words[0]
#     last_word = words[-1]

#     print(f"➡ First word: '{first_word}', Last word: '{last_word}'")

#     start_span = find_word_span(box_entries, first_word, box_pointer)
#     if not start_span:
#         print(f"❌ Couldn't match first word '{first_word}'")
#         continue
#     start_idx = start_span[0]

#     end_span = find_word_span(box_entries, last_word, start_idx)
#     if not end_span:
#         print(f"❌ Couldn't match last word '{last_word}'")
#         continue
#     end_idx = end_span[1]

#     line_boxes = box_entries[start_idx:end_idx + 1]
#     print(f"✅ Found box index span: {start_idx} to {end_idx}")

#     # --- Calculate cropping box using the updated logic ---
#     first_char = line_boxes[0]
#     last_char = line_boxes[-1]

#     x1 = first_char["x"] - horizontal_pad
#     x2 = last_char["x"] + last_char["w"] + horizontal_pad

#     # Get vertical bounds from tallest character in the line
#     top = min(box["y"] for box in line_boxes) - vertical_pad
#     bottom = max(box["y"] + box["h"] for box in line_boxes) + vertical_pad

#     # Clamp to image boundaries
#     x1 = max(x1, 0)
#     x2 = min(x2, image.width)
#     top = max(top, 0)
#     bottom = min(bottom, image.height)

#     print(f"🖼️ Cropping image: x1={x1}, x2={x2}, top={top}, bottom={bottom}")

#     # Crop and save
#     cropped = image.crop((x1, top, x2, bottom))
#     cropped_path = os.path.join(output_dir, f"{base_name}-line{i}.tif")
#     cropped.save(cropped_path)

#     # Save GT line
#     gt_path = os.path.join(output_dir, f"{base_name}-line{i}.gt.txt")
#     with open(gt_path, "w", encoding="utf-8") as f:
#         f.write(line + "\n")

#     # Save .box file (repositioned relative to cropped image)
#     box_path = os.path.join(output_dir, f"{base_name}-line{i}.box")
#     with open(box_path, "w", encoding="utf-8") as f:
#         for b in line_boxes:
#             new_x = b["x"] - x1
#             new_y = b["y"] - top
#             f.write(f"{b['char']} {new_x} {new_y} {b['w']} {b['h']} 0\n")

#     box_pointer = end_idx + 1
#     print(f"💾 Saved line {i} → .tif, .gt.txt, .box")

# print(f"\n✅ Done! All cropped lines saved in: {output_dir}/")

import os
from PIL import Image

# === CONFIG ===
base_name = "page_001"
box_file = f"{base_name}.box"
image_file = f"{base_name}.tif"
gt_file = f"{base_name}.gt.txt"
output_dir = f"{base_name}_lines"
horizontal_pad = 5  # padding for left/right
vertical_pad = 5    # padding for top/bottom

os.makedirs(output_dir, exist_ok=True)

# Load image
image = Image.open(image_file)
img_height = image.height

# Load .box file
with open(box_file, "r", encoding="utf-8") as f:
    raw_boxes = f.readlines()

box_entries = []
for line in raw_boxes:
    parts = line.strip().split()
    if len(parts) == 6:
        char, x1, y1, x2, y2, _ = parts
        box_entries.append({
            "char": char,
            "x1": int(x1),
            "y1": int(y1),  # bottom
            "x2": int(x2),
            "y2": int(y2)   # top
        })

# Load GT lines
with open(gt_file, "r", encoding="utf-8") as f:
    gt_lines = [line.strip() for line in f if line.strip()]

# Match word spans
def find_word_span(entries, target, start=0):
    buffer = ""
    for i in range(start, len(entries)):
        buffer += entries[i]["char"]
        if buffer == target:
            return i - len(target) + 1, i
        elif not target.startswith(buffer):
            buffer = ""
    return None

# Process each GT line
box_pointer = 0
for i, line in enumerate(gt_lines):
    print(f"\n🔍 Processing line {i}: {line}")
    words = line.split()
    if not words:
        continue
    first_word = words[0]
    last_word = words[-1]

    print(f"➡ Matching '{first_word}' → '{last_word}'")

    start_span = find_word_span(box_entries, first_word, box_pointer)
    if not start_span:
        print(f"❌ Couldn't find first word '{first_word}'")
        continue
    start_idx = start_span[0]

    end_span = find_word_span(box_entries, last_word, start_idx)
    if not end_span:
        print(f"❌ Couldn't find last word '{last_word}'")
        continue
    end_idx = end_span[1]

    line_boxes = box_entries[start_idx:end_idx + 1]
    print(f"✅ Characters matched from index {start_idx} to {end_idx}")

    # Calculate box bounds
    x1 = min(b["x1"] for b in line_boxes) - horizontal_pad
    x2 = max(b["x2"] for b in line_boxes) + horizontal_pad
    y1 = min(b["y1"] for b in line_boxes) - vertical_pad  # bottom
    y2 = max(b["y2"] for b in line_boxes) + vertical_pad  # top

    # Clamp to image boundaries
    x1 = max(0, x1)
    x2 = min(image.width, x2)
    y1 = max(0, y1)
    y2 = min(image.height, y2)

    # Convert Tesseract box coords (bottom-left origin) to PIL crop (top-left origin)
    pil_top = img_height - y2
    pil_bottom = img_height - y1

    print(f"🖼️ Cropping image: x=({x1}, {x2}), y=({y1}, {y2}) → PIL: top={pil_top}, bottom={pil_bottom}")

    # Crop image
    cropped = image.crop((x1, pil_top, x2, pil_bottom))
    cropped_path = os.path.join(output_dir, f"{base_name}-line{i}.tif")
    cropped.save(cropped_path)

    # Save GT text
    with open(os.path.join(output_dir, f"{base_name}-line{i}.gt.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Save box file relative to cropped image
    box_path = os.path.join(output_dir, f"{base_name}-line{i}.box")
    with open(box_path, "w", encoding="utf-8") as f:
        for b in line_boxes:
            rel_x1 = b["x1"] - x1
            rel_x2 = b["x2"] - x1
            rel_y1 = img_height - b["y1"] - pil_top  # flip Y
            rel_y2 = img_height - b["y2"] - pil_top  # flip Y
            f.write(f"{b['char']} {rel_x1} {rel_y1} {rel_x2} {rel_y2} 0\n")

    box_pointer = end_idx + 1
    print(f"💾 Saved line {i} → {base_name}-line{i}.tif / .gt.txt / .box")

    # Debug crops of a few individual characters
debug_dir = os.path.join(output_dir, "debug_chars", f"line{i}")
os.makedirs(debug_dir, exist_ok=True)

debug_chars = line_boxes[:3] + line_boxes[-3:]  # first 3 + last 3 chars
for j, b in enumerate(debug_chars):
    rel_x1 = b["x1"] - x1
    rel_x2 = b["x2"] - x1
    rel_y1 = img_height - b["y1"] - pil_top
    rel_y2 = img_height - b["y2"] - pil_top

    char_crop = cropped.crop((rel_x1, rel_y2, rel_x2, rel_y1))
    filename = f"char_{j}_{b['char']}.png"
    char_crop.save(os.path.join(debug_dir, filename))


print(f"\n✅ DONE: All lines saved in: {output_dir}/")
