import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

ADMIN_CHAT_ID = 8758621220

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
    user = update.effective_user
    text = update.message.text

    # မင်းဆီ Order ပို့
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"📩 New Order\n\n👤 {user.full_name}\n🆔 {user.id}\n\n{text}"
    )

    # Customer ကို Reply
    await update.message.reply_text(
        "✅ Order လက်ခံရရှိပါပြီ\n"
        "စစ်ဆေးပြီး အမြန်ဆုံး ပြန်လည်ဆောင်ရွက်ပေးပါမယ်။\n\n"
        + PAYMENT
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_order))

    app.run_polling()

if __name__ == "__main__":
    main()
