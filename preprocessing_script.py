from pdf2image import convert_from_path
from PIL import Image
import os

pdf_path = "my-raw-training-data/twi_dict_17-19.pdf"           
output_folder = "my-raw-training-data"         
dpi = 300                               

os.makedirs(output_folder, exist_ok=True)


print("Converting PDF to images...")
images = convert_from_path(pdf_path, dpi=dpi)

for i, img in enumerate(images):
    gray = img.convert('L')
    
    bw = gray.point(lambda x: 0 if x < 180 else 255, '1') 

    filename = os.path.join(output_folder, f"page_{i+1:03}.tif")
    bw.save(filename, dpi=(300, 300))
    print(f"Saved: {filename}")

