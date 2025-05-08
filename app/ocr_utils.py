from pdf2image import convert_from_path
import pytesseract

# Путь к установленному Poppler — укажи точный путь, где находится `pdftoppm`
POPPLER_PATH = "/opt/homebrew/bin"

# Путь к Tesseract, если требуется указать явно
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text_from_pdf(pdf_path):
    try:
        images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image, lang="deu") + "\n"
        return text.strip()
    except Exception as e:
        print(f"Fehler bei der Texterkennung: {e}")
        return None