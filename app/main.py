from ocr_utils import extract_text_from_pdf
from analyzer import analyze_text
from response_generator import generate_client_response, generate_jobcenter_letter

# Замените путь на актуальный, если файл в другом месте
text = extract_text_from_pdf("/Users/respectgp/PycharmProjects/BuergergeldChatbot/app/bescheid.pdf")

if text:
    problem = analyze_text(text)
    print("Ответ клиенту:")
    print(generate_client_response(problem))
    print("\nПисьмо в Jobcenter:")
    print(generate_jobcenter_letter(problem))
else:
    print("Ошибка: не удалось извлечь текст из PDF.")