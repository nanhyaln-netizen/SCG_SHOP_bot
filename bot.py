import os
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
ADMIN_CHAT_ID = 8758621220

PAYMENT = """
💳 Payment

KPay : 09984759970
Wave Pay : 09984759970
"""

USER_MAP = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    USER_MAP[update.effective_user.id] = update.effective_chat.id

    await update.message.reply_text(
        """
🏪 SCG SHOP

မင်္ဂလာပါ 👋

🎮 PUBG + MLBB Order မှာယူနိုင်ပါတယ်။

📩 Order ပို့ရန်

🎮 Game :
🆔 Game ID :
🌐 Server :
📦 Package :
📸 Payment Screenshot :
"""
    )async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    USER_MAP[user.id] = chat_id

    # Text Message
    if update.message.text:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"""📩 New Order

👤 Name : {user.full_name}
🆔 User ID : {user.id}
📱 Username : @{user.username or 'None'}

💬 Message:
{update.message.text}
"""
        )

    # Photo Message
    elif update.message.photo:
        photo = update.message.photo[-1].file_id
        caption = update.message.caption or "No Caption"

        await context.bot.send_photo(
            chat_id=ADMIN_CHAT_ID,
            photo=photo,
            caption=f"""📸 Payment Screenshot

👤 Name : {user.full_name}
🆔 User ID : {user.id}
📱 Username : @{user.username or 'None'}

📝 Caption:
{caption}
"""
        )

    await update.message.reply_text(
        "✅ Order လက်ခံရရှိပါပြီ\n\n"
        "Admin မှ စစ်ဆေးပြီး အမြန်ဆုံးဆောင်ရွက်ပေးပါမယ်။\n\n"
        + PAYMENT
    )async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Admin မဟုတ်ရင် မလုပ်
    if update.effective_user.id != ADMIN_CHAT_ID:
        return

    # Admin က Reply လုပ်ထားတဲ့ message ဖြစ်ရမယ်
    if not update.message.reply_to_message:
        return

    text = update.message.reply_to_message.text or update.message.reply_to_message.caption or ""

    # User ID ကို ရှာ
    import re
    match = re.search(r"User ID : (\d+)", text)

    if not match:
        return

    user_id = int(match.group(1))

    # Customer ဆီ Reply ပြန်ပို့
    await context.bot.send_message(
        chat_id=user_id,
        text=f"💬 Admin Reply\n\n{update.message.text}"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            (filters.TEXT | filters.PHOTO) & ~filters.COMMAND,
            handle_message,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.REPLY & filters.TEXT,
            admin_reply,
        )
    )

    print("✅ SCG SHOP Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
