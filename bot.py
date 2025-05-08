# bot.py

import os
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

from app.ocr_utils import extract_text_from_pdf, extract_text_from_image
from app.response_generator import explain_problem, generate_jobcenter_letter

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Кнопки «Начать» / «Завершить»
REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [["Начать бот", "Завершить бот"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "Здравствуйте, чем могу помочь? "
        "(напишите свой вопрос или пришлите файл с письмом)",
        reply_markup=REPLY_KEYBOARD
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    user_data = context.user_data

    # Если мы уже ждём от пользователя его текста для письма
    if user_data.get("await_letter_text"):
        user_answer = update.message.text.strip()
        # генерируем письмо на немецком
        letter = generate_jobcenter_letter(user_answer)
        await update.message.reply_text("✅ Вот ваше письмо в Jobcenter:\n\n" + letter)
        user_data.clear()
        return

    # Если мы спросили «Хотите ли вы письмо?» и ждём «да»/«нет»
    if user_data.get("await_letter"):
        if text in ("да", "д", "yes", "y"):
            user_data.pop("await_letter")
            user_data["await_letter_text"] = True
            await update.message.reply_text(
                "Хорошо. Напишите, пожалуйста, что именно вы хотите сообщить в ответном письме."
            )
        else:
            user_data.clear()
            await update.message.reply_text("Понял, письмо не готовим.")
        return

    # Общие команды
    if "начать" in text:
        await update.message.reply_text("Пришлите PDF или фото письма из Jobcenter.")
    elif "завершить" in text:
        await update.message.reply_text("Бот завершён. Спасибо за использование!")
        context.user_data.clear()
    else:
        await update.message.reply_text("Пожалуйста, отправьте PDF или изображение письма.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    file = await update.message.document.get_file()
    file_path = f"app/{update.message.document.file_name}"
    await file.download_to_drive(file_path)

    await update.message.reply_text("📄 Изучаю письмо…")
    text = extract_text_from_pdf(file_path)
    if not text:
        await update.message.reply_text("❌ Не удалось распознать текст. Попробуйте другой файл.")
        return

    explanation = explain_problem(text)
    await update.message.reply_text(
        f"📌 В письме указано:\n\n{explanation}\n\n"
        "Хотите, чтобы я подготовил ответное письмо?"
    )
    user_data["await_letter"] = True

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    photo = update.message.photo[-1]
    file = await photo.get_file()
    file_path = "app/received_image.jpg"
    await file.download_to_drive(file_path)

    await update.message.reply_text("🖼️ Изучаю изображение…")
    text = extract_text_from_image(file_path)
    if not text:
        await update.message.reply_text("❌ Не удалось распознать текст на изображении.")
        return

    explanation = explain_problem(text)
    await update.message.reply_text(
        f"📌 В письме указано:\n\n{explanation}\n\n"
        "Хотите, чтобы я подготовил ответное письмо?"
    )
    user_data["await_letter"] = True

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_document))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Бот запущен...")
    app.run_polling()