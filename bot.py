import telebot
from telebot import types
import random
import time
import sqlite3

TOKEN = "8933077371:AAGjrMQYDJFORak5oOsDiShFu2kg6b0CTXY"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# =========================
# DATABASE
# =========================

db = sqlite3.connect("gym.db", check_same_thread=False)
sql = db.cursor()

sql.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    text TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()

training_log = {}

# =========================
# МОТИВАЦИЯ
# =========================

quotes = [
    "🔥 Ты становишься сильнее каждый день.",
    "💪 Дисциплина создает результат.",
    "🏆 Не сдавайся после тяжелого дня.",
    "⚡ Тренируйся как чемпион.",
    "🔥 Если у тебя поперло, не смей блять остановиться",
    "📈 Дело пошло - сделай все, чтобы преумножить и сохранить",
    "⛔ Не проеби момент"
]

# =========================
# FULL BODY DAYS
# =========================

fullbody_days = {

    "fb_monday":
        "🏋️ <b>FULL BODY • ПОНЕДЕЛЬНИК</b>\n\n"

        "1️⃣ <b>Разминка</b>\n"
        "• Суставная — 10-15 минут\n"
        "• Гиперэкстензии — 10-15 повторений\n"
        "• Разминка связок запястий\n\n"

        "2️⃣ Бабочка — 2x10\n"
        "3️⃣ Жим в Смите на наклонной — 3x10\n"
        "4️⃣ Жим ногами — 3x8\n"
        "5️⃣ Тяга верхнего блока — 3x10\n"
        "6️⃣ Махи в кроссовере — 3x10\n"
        "7️⃣ Бицепс Скотта — 3x10\n"
        "8️⃣ Брусья — 2x15\n\n"

        "🔻 <b>Разминка</b>\n"
        "• Подтягивания\n"
        "• Вис на турнике",

    "fb_wednesday":
        "⚡ <b>FULL BODY • СРЕДА</b>\n\n"

        "1️⃣ <b>Разминка</b>\n"
        "• Суставная — 10-15 минут\n"
        "• Гиперэкстензии — 10-15 повторений\n\n"

        "2️⃣ Подтягивания в гравитроне — 3x15\n"
        "3️⃣ Тяга в хаммере — 3x10\n"
        "4️⃣ Жим в хаммере — 3x10\n"
        "5️⃣ Трицепс — 3x10\n"
        "6️⃣ Задняя часть бедра — 2x10\n"
        "7️⃣ Пуловер — 2x8\n\n"

        "🔻 <b>Разминка</b>\n"
        "• Подтягивания\n"
        "• Вис на турнике",

    "fb_friday":
        "🏆 <b>FULL BODY • ПЯТНИЦА</b>\n\n"

        "1️⃣ <b>Разминка</b>\n"
        "• Суставная — 10-15 минут\n"
        "• Гиперэкстензии — 10-15 повторений\n\n"

        "2️⃣ Жим ногами — 3x10\n"
        "3️⃣ Жим лёжа — 2x8\n"
        "4️⃣ Икры — 3x15-20\n"
        "5️⃣ Разгибания квадрицепса — 3x10\n"
        "6️⃣ Подтягивания — 3x10\n\n"

        "🔻 <b>Разминка</b>\n"
        "• Подтягивания\n"
        "• Вис на турнике"
}

# =========================
# START
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📋 Меню")

    text = (
        "🏋️ <b>IRON GYM</b>\n\n"
        "🔥 Добро пожаловать в систему тренировок\n\n"
        "⚡ Становись сильнее каждый день\n\n"
        "👇 Открой меню"
    )

    try:
        bot.send_photo(
            message.chat.id,
            open("banner.jpg", "rb"),
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
# MENU
# =========================

@bot.message_handler(func=lambda m: m.text == "📋 Меню")
def menu(message):

    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.add(
        types.InlineKeyboardButton("🏋️ Программы", callback_data="programs"),
        types.InlineKeyboardButton("🍗 Питание", callback_data="food")
    )

    kb.add(
        types.InlineKeyboardButton("🔥 Мотивация", callback_data="motivation"),
        types.InlineKeyboardButton("📈 Записать", callback_data="progress")
    )

    kb.add(
        types.InlineKeyboardButton("📒 Дневник", callback_data="log"),
        types.InlineKeyboardButton("💎 VIP", callback_data="vip")
    )

    kb.add(
        types.InlineKeyboardButton(
            "🔥 GYM DEMONS",
            url="https://t.me/GYMDEMONS"
        )
    )

    text = (
        "🔥 <b>IRON GYM PANEL</b>\n\n"
        "🏋️ Выбери нужный раздел\n"
        "⚡ Всё для твоего прогресса"
    )

    try:
        bot.send_photo(
            message.chat.id,
            open("banner.jpg", "rb"),
            caption=text,
            reply_markup=kb
        )
    except:
        bot.send_message(
            message.chat.id,
            text,
            reply_markup=kb
        )

# =========================
# CALLBACK
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    user_id = call.from_user.id

    # =====================
    # ПРОГРАММЫ
    # =====================

    if call.data == "programs":

        kb = types.InlineKeyboardMarkup(row_width=1)

        kb.add(
            types.InlineKeyboardButton(
                "🏋️ FULL BODY",
                callback_data="fullbody"
            ),

            types.InlineKeyboardButton(
                "🔥 SPLIT",
                callback_data="split"
            ),

            types.InlineKeyboardButton(
                "⚡ ВЕРХ / НИЗ",
                callback_data="upperlower"
            ),

            types.InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="back"
            )
        )

        bot.send_message(
            call.message.chat.id,
            "🏋️ <b>ПРОГРАММЫ ТРЕНИРОВОК</b>\n\n"
            "Выбери тип тренировок 👇",
            reply_markup=kb
        )

    # =====================
    # FULL BODY MENU
    # =====================

    elif call.data == "fullbody":

        kb = types.InlineKeyboardMarkup(row_width=1)

        kb.add(
            types.InlineKeyboardButton(
                "🔥 ПОНЕДЕЛЬНИК",
                callback_data="fb_monday"
            ),

            types.InlineKeyboardButton(
                "⚡ СРЕДА",
                callback_data="fb_wednesday"
            ),

            types.InlineKeyboardButton(
                "🏆 ПЯТНИЦА",
                callback_data="fb_friday"
            ),

            types.InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="programs"
            )
        )

        bot.send_message(
            call.message.chat.id,
            "🏋️ <b>FULL BODY</b>\n\n"
            "Выбери тренировочный день 👇",
            reply_markup=kb
        )

    # =====================
    # FULL BODY DAYS
    # =====================

    elif call.data in fullbody_days:

        bot.send_message(
            call.message.chat.id,
            fullbody_days[call.data]
        )

    # =====================
    # SPLIT
    # =====================

    elif call.data == "split":

        text = (
            "🔥 <b>SPLIT</b>\n\n"

            "📅 ПН — Грудь\n"
            "📅 СР — Спина\n"
            "📅 ПТ — Ноги\n\n"

            "💪 Идеально для массы и силы"
        )

        bot.send_message(call.message.chat.id, text)

    # =====================
    # UPPER LOWER
    # =====================

    elif call.data == "upperlower":

        text = (
            "⚡ <b>ВЕРХ / НИЗ</b>\n\n"

            "📅 ПН — Верх\n"
            "📅 СР — Низ\n"
            "📅 ПТ — Верх\n\n"

            "🔥 Баланс нагрузки и восстановления"
        )

        bot.send_message(call.message.chat.id, text)

    # =====================
    # FOOD
    # =====================

    elif call.data == "food":

        text = (
            "🍗 <b>ПИТАНИЕ ПО ПРОГРАММАМ</b>\n\n"

            "🏋️ FULL BODY\n"
            "• Белок 2г/кг\n"
            "• Средние углеводы\n"
            "• Лёгкий профицит\n\n"

            "🔥 SPLIT\n"
            "• Белок 2.2г/кг\n"
            "• Высокие углеводы\n"
            "• Масса\n\n"

            "⚡ ВЕРХ / НИЗ\n"
            "• Белок 2г/кг\n"
            "• Баланс\n\n"

            "💧 Вода 2-3л\n"
            "😴 Сон 7-9 часов"
        )

        bot.send_message(call.message.chat.id, text)

    # =====================
    # MOTIVATION
    # =====================

    elif call.data == "motivation":

        bot.send_message(
            call.message.chat.id,
            random.choice(quotes)
        )

    # =====================
    # VIP
    # =====================

    elif call.data == "vip":

        text = (
            "💎 <b>VIP ТРЕНИРОВКИ</b>\n\n"

            "👨‍🏫 Тренер: @VVV_Naz\n\n"

            "🔥 <b>Что ты получишь:</b>\n"
            "• Индивидуальный план\n"
            "• Исправление техники\n"
            "• Контроль прогресса\n"
            "• Питание под цель\n"
            "• Дисциплину и мотивацию\n\n"

            "💪 Это уже другой уровень тренировок"
        )

        bot.send_message(
            call.message.chat.id,
            text
        )

    # =====================
    # ПРОГРЕСС
    # =====================

    elif call.data == "progress":

        training_log[user_id] = True

        bot.send_message(
            call.message.chat.id,
            "📈 <b>ЗАПИСЬ ТРЕНИРОВКИ</b>\n\n"
            "✍️ Напиши что ты сделал сегодня\n\n"
            "Пример:\n"
            "Жим 70кг 4х10"
        )

    # =====================
    # ДНЕВНИК
    # =====================

    elif call.data == "log":

        sql.execute(
            "SELECT text, date FROM logs WHERE user_id=? ORDER BY id DESC LIMIT 5",
            (user_id,)
        )

        data = sql.fetchall()

        if not data:

            text = "📒 <b>ДНЕВНИК ПУСТ</b>"

        else:

            text = "📒 <b>ПОСЛЕДНИЕ ТРЕНИРОВКИ</b>\n\n"

            for i in data:
                text += f"🗓 {i[1]}\n🏋️ {i[0]}\n\n"

        bot.send_message(
            call.message.chat.id,
            text
        )

    # =====================
    # BACK
    # =====================

    elif call.data == "back":

        menu(call.message)

# =========================
# SAVE TRAINING
# =========================

@bot.message_handler(func=lambda m: True)
def save_training(message):

    user_id = message.from_user.id

    if user_id in training_log:

        sql.execute(
            "INSERT INTO logs (user_id, text) VALUES (?,?)",
            (user_id, message.text)
        )

        db.commit()

        del training_log[user_id]

        bot.send_message(
            message.chat.id,
            "✅ ТРЕНИРОВКА СОХРАНЕНА В ДНЕВНИК"
        )

# =========================
# RUN
# =========================

print("BOT STARTED 🚀")

while True:

    try:

        bot.infinity_polling()

    except Exception as e:

        print(e)
        time.sleep(3)