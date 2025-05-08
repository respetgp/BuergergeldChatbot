import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

from app.ocr_utils import extract_text_from_pdf
from app.analyzer import analyze_text
from app.response_generator import generate_client_response, generate_jobcenter_letter

# Загружаем переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the .env file")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Пришлите PDF или фото письма из Jobcenter.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_path = f"app/{update.message.document.file_name}"
    await file.download_to_drive(file_path)

    text = extract_text_from_pdf(file_path)
    if not text:
        await update.message.reply_text("Не удалось распознать текст. Пожалуйста, проверьте качество файла.")
        return

    problem = analyze_text(text)
    user_msg = generate_client_response(problem)
    letter = generate_jobcenter_letter(problem)

    await update.message.reply_text(f"Ответ клиенту:\n{user_msg}\n\nПисьмо в Jobcenter:\n{letter}")

if __name__ == "__main__":
    print("Бот запущен...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_document))
    app.run_polling()