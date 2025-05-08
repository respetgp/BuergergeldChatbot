from app.ocr_utils import extract_text_from_image

if __name__ == "__main__":
    result = extract_text_from_image("example_letter.jpg")  # замени на путь к своему скану
    print(result)