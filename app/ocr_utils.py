import os
from dotenv import load_dotenv
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

load_dotenv()

# Если у вас Poppler установлен в нестандартном месте, укажите его через переменную окружения POPPLER_PATH
POPPLER_PATH = os.getenv("POPPLER_PATH", None)


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Конвертирует PDF в изображения и распознаёт текст (немецкий язык).
    """
    try:
        # Если задан POPPLER_PATH, передаём его в convert_from_path
        if POPPLER_PATH:
            images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
        else:
            images = convert_from_path(pdf_path)
    except Exception as e:
        print(f"Fehler beim Konvertieren PDF→Bilder: {e}")
        return ""

    text = ""
    for img in images:
        try:
            text += pytesseract.image_to_string(img, lang="deu") + "\n"
        except Exception as e:
            print(f"Fehler bei OCR eines Bildes: {e}")
    return text.strip()


def extract_text_from_image(image_path: str) -> str:
    """
    Распознаёт текст на изображении (немецкий язык).
    """
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img, lang="deu").strip()
    except Exception as e:
        print(f"Fehler bei OCR des Bildes: {e}")
        return ""