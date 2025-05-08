from PIL import Image
import pytesseract

def extract_text_from_image(image_path: str) -> str:
    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang='deu')  # используем немецкий
        return text.strip()
    except Exception as e:
        return f"Fehler bei der Texterkennung: {e}"