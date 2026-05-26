import telebot
from telebot import types
import random
import time
import os

# =========================
# TOKEN
# =========================

TOKEN = os.getenv("8933077371:AAGjrMQYDJFORak5oOsDiShFu2kg6b0CTXY")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# =========================
# МОТИВАЦИЯ
# =========================

quotes = [
    "🔥 Ты становишься сильнее каждый день.",
    "💪 Дисциплина создает результат.",
    "🏆 Не сдавайся после тяжелого дня.",
    "⚡ Тренируйся как чемпион.",
    "🔥 Если у тебя поперло, не смей блять остановиться\n\nДело пошло — сделай всё, чтобы преумножить и сохранить.\n\nНе проеби момент."
]

# =========================
# START
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu_btn = types.KeyboardButton("📋 Меню")

    markup.add(menu_btn)

    text = (
        "🏋️ <b>IRON GYM</b>\n\n"
        "🔥 Добро пожаловать в лучший фитнес-бот\n\n"
        "Нажми кнопку ниже 👇"
    )

    try:

        photo = open("banner.jpg", "rb")

        bot.send_photo(
            message.chat.id,
            photo,
            caption=text,
            reply_markup=markup
        )

    except:

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=markup
        )

# =========================
# ГЛАВНОЕ МЕНЮ
# =========================

@bot.message_handler(func=lambda message: message.text == "📋 Меню")
def menu(message):

    inline = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton(
        "🏋️ Программы",
        callback_data="programs"
    )

    btn2 = types.InlineKeyboardButton(
        "🍗 Питание",
        callback_data="food"
    )

    btn3 = types.InlineKeyboardButton(
        "📖 Дневник",
        callback_data="diary"
    )

    btn4 = types.InlineKeyboardButton(
        "🔥 Мотивация",
        callback_data="motivation"
    )

    btn5 = types.InlineKeyboardButton(
        "💎 VIP",
        callback_data="vip"
    )

    btn6 = types.InlineKeyboardButton(
        "⚔️ GYM DEMONS",
        url="https://t.me/GYMDEMONS"
    )

    inline.add(btn1, btn2)
    inline.add(btn3, btn4)
    inline.add(btn5)
    inline.add(btn6)

    text = (
        "🏋️ <b>IRON GYM</b>\n\n"
        "🔥 Выбери нужный раздел"
    )

    try:

        photo = open("banner.jpg", "rb")

        bot.send_photo(
            message.chat.id,
            photo,
            caption=text,
            reply_markup=inline
        )

    except:

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=inline
        )

# =========================
# CALLBACK
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # =====================
    # ПРОГРАММЫ
    # =====================

    if call.data == "programs":

        inline = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            "🏋️ Full Body",
            callback_data="fullbody"
        )

        btn2 = types.InlineKeyboardButton(
            "🔥 Split",
            callback_data="split"
        )

        btn3 = types.InlineKeyboardButton(
            "⚡ Верх / Низ",
            callback_data="upperlower"
        )

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )

        inline.add(btn1, btn2, btn3, back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="🏋️ <b>ПРОГРАММЫ ТРЕНИРОВОК</b>\n\nВыбери программу:",
            reply_markup=inline
        )

    # =====================
    # FULL BODY
    # =====================

    elif call.data == "fullbody":

        inline = types.InlineKeyboardMarkup(row_width=1)

        mon = types.InlineKeyboardButton(
            "📅 Понедельник",
            callback_data="fb_mon"
        )

        wed = types.InlineKeyboardButton(
            "📅 Среда",
            callback_data="fb_wed"
        )

        fri = types.InlineKeyboardButton(
            "📅 Пятница",
            callback_data="fb_fri"
        )

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="programs"
        )

        inline.add(mon, wed, fri, back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="🏋️ <b>FULL BODY</b>\n\nВыбери день тренировки:",
            reply_markup=inline
        )

    # =====================
    # FULL BODY ПОНЕДЕЛЬНИК
    # =====================

    elif call.data == "fb_mon":

        text = (
            "🏋️ <b>FULL BODY — ПОНЕДЕЛЬНИК</b>\n\n"

            "1️⃣ Разминка\n"
            "• Суставная 10-15 минут\n"
            "• Гиперэкстензии 10-15\n"
            "• Разминка запястий\n\n"

            "2️⃣ Бабочка — 2x10\n"
            "3️⃣ Жим в Смите — 3x10\n"
            "4️⃣ Жим ногами — 3x8\n"
            "5️⃣ Тяга верхнего блока — 3x10\n"
            "6️⃣ Махи в кроссовере — 3x10\n"
            "7️⃣ Бицепс Скотта — 3x10\n"
            "8️⃣ Брусья — 2x15\n\n"

            "🔥 Заминка 5-10 минут"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="fullbody"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # FULL BODY СРЕДА
    # =====================

    elif call.data == "fb_wed":

        text = (
            "🏋️ <b>FULL BODY — СРЕДА</b>\n\n"

            "1️⃣ Разминка\n"
            "• Суставная 10-15 минут\n"
            "• Гиперэкстензии\n\n"

            "2️⃣ Гравитрон — 3x15\n"
            "3️⃣ Тяга в хаммере — 3x10\n"
            "4️⃣ Жим в хаммере — 3x10\n"
            "5️⃣ Трицепс — 3x10\n"
            "6️⃣ Задняя часть бедра — 2x10\n"
            "7️⃣ Пуловер — 2x8\n\n"

            "🔥 Заминка 5-10 минут"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="fullbody"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # FULL BODY ПЯТНИЦА
    # =====================

    elif call.data == "fb_fri":

        text = (
            "🏋️ <b>FULL BODY — ПЯТНИЦА</b>\n\n"

            "1️⃣ Разминка\n"
            "• Суставная 10-15 минут\n"
            "• Гиперэкстензии\n\n"

            "2️⃣ Жим ногами — 3x10\n"
            "3️⃣ Жим лёжа — 2x8\n"
            "4️⃣ Икры — 3x20\n"
            "5️⃣ Разгибания квадрицепса — 3x10\n"
            "6️⃣ Подтягивания — 3x10\n\n"

            "🔥 Заминка 5-10 минут"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="fullbody"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # SPLIT
    # =====================

    elif call.data == "split":

        text = (
            "🔥 <b>SPLIT</b>\n\n"
            "ПН — Грудь\n"
            "СР — Спина\n"
            "ПТ — Ноги"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="programs"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # UPPER LOWER
    # =====================

    elif call.data == "upperlower":

        text = (
            "⚡ <b>ВЕРХ / НИЗ</b>\n\n"
            "ПН — Верх тела\n"
            "СР — Низ тела\n"
            "ПТ — Верх тела"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="programs"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # ПИТАНИЕ
    # =====================

    elif call.data == "food":

        text = (
            "🍗 <b>ПИТАНИЕ</b>\n\n"

            "🏋️ Full Body\n"
            "• Белок — 2г/кг\n"
            "• Больше углеводов\n"
            "• Вода — 3л\n\n"

            "🔥 Split\n"
            "• Профицит калорий\n"
            "• Много белка\n"
            "• Сон — 8 часов\n\n"

            "⚡ Верх / Низ\n"
            "• Баланс БЖУ\n"
            "• Овощи каждый день\n"
            "• Контроль воды"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # ДНЕВНИК
    # =====================

    elif call.data == "diary":

        text = (
            "📖 <b>ДНЕВНИК ТРЕНИРОВОК</b>\n\n"
            "✍️ Напиши свою тренировку следующим сообщением.\n\n"
            "Например:\n"
            "• Жим 80x8\n"
            "• Присед 100x5"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # МОТИВАЦИЯ
    # =====================

    elif call.data == "motivation":

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=random.choice(quotes),
            reply_markup=inline
        )

    # =====================
    # VIP
    # =====================

    elif call.data == "vip":

        text = (
            "💎 <b>VIP ТРЕНИРОВКИ</b>\n\n"

            "🔥 Индивидуальный подход\n"
            "🔥 Программа под тебя\n"
            "🔥 Контроль прогресса\n"
            "🔥 Питание и рекомендации\n"
            "🔥 Поддержка и мотивация\n\n"

            "⚔️ <b>@VVV_Naz</b>"
        )

        inline = types.InlineKeyboardMarkup()

        back = types.InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )

        inline.add(back)

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

    # =====================
    # НАЗАД
    # =====================

    elif call.data == "back":

        inline = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            "🏋️ Программы",
            callback_data="programs"
        )

        btn2 = types.InlineKeyboardButton(
            "🍗 Питание",
            callback_data="food"
        )

        btn3 = types.InlineKeyboardButton(
            "📖 Дневник",
            callback_data="diary"
        )

        btn4 = types.InlineKeyboardButton(
            "🔥 Мотивация",
            callback_data="motivation"
        )

        btn5 = types.InlineKeyboardButton(
            "💎 VIP",
            callback_data="vip"
        )

        btn6 = types.InlineKeyboardButton(
            "⚔️ GYM DEMONS",
            url="https://t.me/GYMDEMONS"
        )

        inline.add(btn1, btn2)
        inline.add(btn3, btn4)
        inline.add(btn5)
        inline.add(btn6)

        text = (
            "🏋️ <b>IRON GYM</b>\n\n"
            "🔥 Выбери нужный раздел"
        )

        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=text,
            reply_markup=inline
        )

# =========================
# СОХРАНЕНИЕ ДНЕВНИКА
# =========================

@bot.message_handler(func=lambda message: True)
def diary_save(message):

    if message.text == "📋 Меню":
        return

    text = (
        "🔥 <b>ТРЕНИРОВКА СОХРАНЕНА</b>\n\n"
        f"{message.text}"
    )

    bot.send_message(message.chat.id, text)

# =========================
# ЗАПУСК
# =========================

print("Бот запущен 🚀")

if __name__ == "__main__":

    while True:

        try:

            bot.infinity_polling(
                timeout=30,
                long_polling_timeout=30,
                skip_pending=True
            )

        except Exception as e:

            print("ОШИБКА:", e)
            time.sleep(3)