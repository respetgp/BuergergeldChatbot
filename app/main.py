# main.py

from app.ocr_utils import extract_text_from_pdf, extract_text_from_image
from app.response_generator import explain_problem, generate_jobcenter_letter

def main():
    # 1) Укажите путь к файлу PDF или изображению:
    file_path = "app/bescheid.pdf"  # либо "app/example.jpg", "app/example.png" и т.п.

    # 2) Распознаём текст
    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    # 3) Проверка
    if not text:
        print("❌ Ошибка: не удалось извлечь текст из файла.")
        return

    # 4) Объясняем пользователю на русском, что в письме
    print("📌 Объяснение для клиента:")
    explanation = explain_problem(text)
    print(explanation)

    # 5) Спрашиваем, готовим ли письмо
    choice = input("\nХотите, чтобы я подготовил письмо в Jobcenter? (y/n): ").strip().lower()
    if choice in ("y", "yes", "д", "да"):
        print("\n📄 Письмо в Jobcenter:")
        letter = generate_jobcenter_letter(text)
        print(letter)
    else:
        print("\nХорошо, письмо не готовим. Вы можете запустить программу снова.")

if __name__ == "__main__":
    main()