import os
from app.ocr_utils import extract_text_from_pdf, extract_text_from_image
from app.response_generator import explain_problem, generate_jobcenter_letter

def main():
    # 1. Запрашиваем путь к файлу
    file_path = input("Введите путь к PDF или изображению: ").strip()

    # 2. Проверяем существование
    if not os.path.exists(file_path):
        print(f"❌ Файл не найден: {file_path}")
        return

    # 3. Определяем тип и извлекаем текст
    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    # 4. Проверка результата
    if not text:
        print("❌ Ошибка: не удалось извлечь текст из файла.")
        return

    # 5. Объяснение на русском
    print("\n📌 Объяснение для клиента:")
    explanation = explain_problem(text)
    print(explanation)

    # 6. Предложение письма
    choice = input("\nХотите, чтобы я подготовил письмо в Jobcenter? (y/n): ").strip().lower()
    if choice in ("y", "yes", "д", "да"):
        print("\n📄 Письмо в Jobcenter:")
        letter = generate_jobcenter_letter(text)
        print(letter)
    else:
        print("\nХорошо, письмо не готовим. Вы можете запустить программу снова.")

if __name__ == "__main__":
    main()