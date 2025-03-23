# 📝 Akan OCR: First Custom OCR Model for the Akan Language

This project contains the first-ever custom-trained **Tesseract OCR model for Twi (Akan)** — one of the most widely spoken languages in Ghana and West Africa.

It was trained using **scanned pages of a Twi dictionary**, with special attention to accented characters (e.g. ɛ, ɔ, ḿ, etc.) that are not well-supported by existing OCR systems.

---

## 💡 Why This Matters

Twi and other Akan languages are deeply rooted in Ghanaian culture and widely spoken, yet they remain underrepresented in digital tools like OCR, speech, and translation systems.

This project:
- Enables automatic text extraction from Twi books, dictionaries, and archives
- Supports accented characters used in phonetic representations
- Lays the foundation for future OCR and NLP tools in Akan languages

---

## 🛠️ What This Repository Includes

- Line-level annotated training data (`.tif`, `.box`, `.gt.txt`)
- Custom character set (`unicharset`)
- Compiled `twi.traineddata` model for use with Tesseract OCR
- Output from the LSTM training process using Tesseract 5.4.1

---

## 🧠 Model Capabilities

- Detects Twi characters and accented symbols
- Trained on dictionary-style formats
- Performs well on clean scans of printed Twi material

---

## 🔬 Technology Stack

- Tesseract OCR 5.4.1
- Python (for data preparation)
- Linux
- Custom training scripts and image pre-processing

---

## 📖 Usage

Once you install Tesseract 5.4.1, copy the `twi.traineddata` file from tesstrain/data/twi-ground-truth folder into your Tesseract `tessdata` folder and run:

```bash
tesseract "{INPUT IMAGE}.tif" stdout -l twi   --oem 1   --tessdata-dir {TESSDATA DIR}   --psm 6

```

---

## ✍️ Author

**Kissi Emmanuel Ankomah**  
Biomedical Engineer | AI Researcher | Software Engineer  
🇬🇭 Ghana  
[GitHub](https://github.com/mister9ce)

---

## 🧡 Acknowledgements

- Based on the Tesseract OCR engine by Google
- Informed by insights from the open-source OCR community
- Inspired by the need to support African languages in modern NLP tools

---

> This is a step toward preserving and empowering African languages with AI.
