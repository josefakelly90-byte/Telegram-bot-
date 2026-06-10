from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("8559497557:AAEl7IHus2kKZKo2a9Fq64YJRKqWc3uPfLc")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm online 24/7 🤖")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
