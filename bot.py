import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

openai.api_key = os.getenv("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")
TELEGRAM_TOKEN = os.getenv("7055101648:AAEROkLHtlps47kNxiBSL7_mw57TZtNnaqU")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    await context.bot.send_message(chat_id=chat_id, text=response['choices'][0]['message']['content'])

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
