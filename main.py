
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

main_menu = ReplyKeyboardMarkup([
    ["📦 Продукція"],
    ["❓ Часті питання", "📞 Контакти"]
], resize_keyboard=True)

product_menu = ReplyKeyboardMarkup([
    ["🩹 Післяопераційні пояси"],
    ["🤰 Бандажі", "🧍 Корсети"],
    ["🧦 Компресійна білизна"],
    ["🩺 Еластичні бинти"],
    ["🛡 Підтримуючі / протирадикулітні пояси"],
    ["🦿 Ортези та еластичні фіксатори"],
    ["⬅️ Назад"]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Вітаємо у довіднику продукції ТМ Лаума!\n\nОберіть дію:",
        reply_markup=main_menu
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 Продукція":
        await update.message.reply_text("Оберіть категорію продукції:", reply_markup=product_menu)

    elif text == "🦿 Ортези та еластичні фіксатори":
        await update.message.reply_photo(
            photo="https://laumamedical.com/uploads/product/large/501-knee-support-1.jpg",
            caption=(
                "*🦿 Ортез колінний 501*\n\n"
                "🔹 *Призначення:* Забезпечує підтримку колінного суглоба при навантаженні або після травм.\n\n"
                "🧵 *Склад:* 60% поліестер, 20% еластан, 20% латекс\n\n"
                "📏 *Розміри (обхват коліна):*\n"
                "- S: 33–36 см\n"
                "- M: 36–39 см\n"
                "- L: 39–42 см\n"
                "- XL: 42–45 см\n\n"
                "📷 [Таблиця розмірів](https://laumamedical.com/uploads/sizechart/501-sizechart.jpg)"
            ),
            parse_mode="Markdown"
        )

    elif text == "❓ Часті питання":
        await update.message.reply_markdown(
            "*Часті питання:*\n\n"
            "1. Де купити продукцію? — У наших партнерів або онлайн.\n"
            "2. Чи є гарантія? — Так, 14 днів на обмін/повернення."
        )

    elif text == "📞 Контакти":
        await update.message.reply_markdown(
            "*Контакти:*\n"
            "🌐 Сайт: https://laumamedical.com/\n"
            "📧 Email: info@laumamedical.com"
        )

    elif text == "⬅️ Назад":
        await update.message.reply_text("Повертаємось до головного меню:", reply_markup=main_menu)

    else:
        await update.message.reply_text("Будь ласка, оберіть дію з меню ⬇️")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
