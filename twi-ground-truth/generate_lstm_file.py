cd page_001_lines
for f in *.tif; do
  base="${f%.tif}"
  tesseract "$f" "$base" --psm 6 lstm.train
done