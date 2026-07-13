import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

PAYMENT = """
💳 Payment

KPay : 09984759970
Wave Pay : 09984759970
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🏪 SCG SHOP

မင်္ဂလာပါ 👋

🎮 PUBG + MLBB Order မှာယူနိုင်ပါတယ်။

Order တင်ရန် ပို့ပေးပါ—

🎮 Game:
🆔 ID:
🌐 Server:
📦 Package:
💳 Payment Screenshot:
""")

async def reply_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    await update.message.reply_text(
        "✅ Order လက်ခံရရှိပါပြီ\n"
        "စစ်ဆေးပြီး အမြန်ဆုံး ပြန်လည်ဆောင်ရွက်ပေးပါမယ်။\n\n"
        + PAYMENT
    )

    # Admin username နေရာကို နောက်မှ User ID ပြောင်းရမယ်

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, reply_order))

    app.run_polling()

if __name__ == "__main__":
    main()