import os
import re
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")

# မင်း Telegram ID
ADMIN_CHAT_ID = 8758621220

PAYMENT = """
💳 Payment

KPay : 09984759970
Wave Pay : 09984759970
"""

# User ID တွေကို သိမ်းထားမယ့် Dictionary
USER_MAP ={}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    USER_MAP[user_id] = True

    await update.message.reply_text(
        "👋 Welcome to SCG SHOP\n\n"
        "💎 UC / Diamond ဝယ်ယူလိုပါက အောက်က menu ကိုအသုံးပြုပါ။\n\n"
        "Payment ကြည့်ရန် /payment ကိုနှိပ်ပါ"
    )


async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PAYMENT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start Bot\n"
        "/payment - Payment Info\n"
        "/help - Help"
 
     )
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "order" in text.lower() or "ဝယ်" in text:
        await update.message.reply_text(
            "🛒 Order တင်လိုပါက\n"
            "Game Name + ID + Server ပို့ပေးပါ။"
        )
    else:
        await update.message.reply_text(
            "SCG SHOP မှ ကြိုဆိုပါတယ် 💎\n"
            "UC / Diamond ဝယ်ယူလိုပါက ဆက်သွယ်ပါ။"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
