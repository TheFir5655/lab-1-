import json, telebot, random, requests, os
from os.path import exists
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

Regular_em = "CAACAgIAAxkBAAE0v0loIDe2ajpsDHPvTiD3dBwRXJuN6gAC1XMAArKS-UiUYk9DL8Hc-TYE"
Hi_em = "CAACAgIAAxkBAAE0vzloIDac8Sy9H9V99RXuhvZLIYdYIwACnGsAAsW7-EhRNn8F8EPMlTYE"
Hand_em = "CAACAgIAAxkBAAE0v0NoIDcAAev_CB6xr63vnFPufyUFm4MAAgtoAAKErPlIRfmgQVOHiDo2BA"
Happy_em = "CAACAgIAAxkBAAE0v09oIDfutWmRwBBNOr1O7N-iDEWPTQACsmwAAic2-EjjCvGs4q3G6DYE"
Yes_em = "CAACAgIAAxkBAAE0v1FoIDgBEn9Gaqcts91N1XqZp_q5wAACN2sAAuiX-UiYaninogfzNDYE"
No_em = "CAACAgIAAxkBAAE0v1NoIDgO304mdgl-iNLNjFJD4c3DfgACI2sAAtwK-EiNvz1iceTE-DYE"
Cunning_em = "CAACAgIAAxkBAAE0v1VoIDgckMaH46DrFG6yPs-D9BvPEAACh3QAAqbH-UhaqUwe71TCSTYE"
Load_em = "CAACAgIAAxkBAAE0v1doIDg0FohXk-7JkxBIJPfo8oXFSwACLHQAAjrs-UjMc84012egNDYE"
Error_em = "CAACAgIAAxkBAAE0v1loIDhGCMUyDfkr26G27K12Qqc3wQACHG4AAv_E-Ej3RJW-mvhQJjYE"
Crystal_ball_em = "CAACAgIAAxkBAAE0v1toIDhT1CNjg-ZqyfBXnEsKaT9A-AAC0G0AAmsV-EjU1BluejEftTYE"

def load_users():
    if exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

users = load_users()

keyword = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyword.row("О боте")
keyword.row("Изменить имя")
keyword.row("Сделать выбор")
keyword.row("Фото лисы")
keyword.row("Стикеры")

def process_name_step(message):
    user_id = str(message.from_user.id)
    name = message.text
    users[user_id] = {
        'name': name,
        'id': user_id
    }
    save_users(users)
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Теперь ты можешь использовать команды:",
                     reply_markup=keyword)
    bot.send_message(message.chat.id,
                     "О боте - о боте\nИзменить имя - как ты хочешь чтоб я тебя называл\nСделать выбор - сделаю за тебя выбор\nФото лисы - скину фоточку лисы\nСтикеры - скину ссылку на свои стикеры!")

def process_username_change(message):
    user_id = str(message.from_user.id)
    new_name = message.text
    if user_id in users:
        users[user_id]['name'] = new_name
        save_users(users)
        bot.send_message(message.chat.id, f"Хорошо, теперь я буду называть тебя {new_name}!")
        bot.send_sticker(message.chat.id, sticker=Yes_em)
    else:
        bot.send_message(message.chat.id, "Сначала используйте команду /start для регистрации.")
        bot.send_sticker(message.chat.id, sticker=Error_em)

def get_random_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        return response.json()["image"]
    return None

def crystal_magic(message):
    user_id = str(message.from_user.id)
    random_num = random.randint(1, 10)
    if user_id in users:
        if random_num == 1:
            bot.send_message(message.chat.id, f"{users[user_id]['name']}, мои источники говорят да")
            bot.send_sticker(message.chat.id, sticker=Yes_em)
        elif random_num == 2:
            bot.send_message(message.chat.id, f"Хмм.. Мои источники говорят нет, {users[user_id]['name']}")
            bot.send_sticker(message.chat.id, sticker=No_em)
        elif random_num == 3:
            bot.send_message(message.chat.id, f"Хмм.. Я думаю да, {users[user_id]['name']}")
            bot.send_sticker(message.chat.id, sticker=Yes_em)
        elif random_num == 4:
            bot.send_message(message.chat.id, f"Скорее нет, не совсем")
            bot.send_sticker(message.chat.id, sticker=No_em)
        elif random_num == 5:
            bot.send_message(message.chat.id, f"Ответ не найден")
            bot.send_sticker(message.chat.id, sticker=Error_em)
        elif random_num in (6, 7, 8):
            bot.send_message(message.chat.id, f"{users[user_id]['name']}, задай вопрос позже, сейчас не время..")
            bot.send_sticker(message.chat.id, sticker=Load_em)
        elif random_num == 9:
            bot.send_sticker(message.chat.id, sticker=Cunning_em)
        else:
            bot.send_message(message.chat.id, f"NameError: name 'answer' is not found\n\nProcess finished with exit code 1")
            bot.send_sticker(message.chat.id, sticker=Error_em)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

@bot.message_handler(commands=["start"])
def welcome(message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        bot.send_sticker(message.chat.id, sticker=Hi_em)
        bot.send_message(message.chat.id, "Привет! Как тебя зовут?", reply_markup=keyword)
        bot.register_next_step_handler(message, process_name_step)
    else:
        bot.send_sticker(message.chat.id, sticker=Hi_em)
        bot.send_message(message.chat.id, f"С возвращением, {users[user_id]['name']}!", reply_markup=keyword)

@bot.message_handler(func=lambda message: message.text == "О боте")
def about(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        bot.send_message(message.chat.id, f"{users[user_id]['name']}, Давай расскажу о себе!")
        bot.send_sticker(message.chat.id, sticker=Hand_em)
        bot.send_message(message.chat.id,
                         f'В мои функции входят:\n\nРеакция стикерами на твои команды.\nМогу помочь определиться с выбором.\nТакже могу скидывать картинки лисов!\nМеня создали @Jam_skrimer и @TheFir565, буду рад служить!')
        bot.send_sticker(message.chat.id, sticker=Happy_em)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

@bot.message_handler(func=lambda message: message.text == "Изменить имя")
def change_username(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        bot.send_message(message.chat.id, "Как ты хочешь, чтобы я тебя называл?")
        bot.register_next_step_handler(message, process_username_change)
        bot.send_sticker(message.chat.id, sticker=Load_em)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

@bot.message_handler(func=lambda message: message.text == "Сделать выбор")
def magic_ball(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        bot.send_message(message.chat.id, "Задай вопрос на который можно ответить да или нет и я решу ответ на этот вопрос с помощью хрустального шара")
        bot.send_sticker(message.chat.id, sticker=Crystal_ball_em)
        bot.register_next_step_handler(message, crystal_magic)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

@bot.message_handler(func=lambda message: message.text == "Фото лисы")
def foxes(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        fox_image_url = get_random_fox_image()
        bot.send_sticker(message.chat.id, sticker=Cunning_em)
        bot.send_photo(message.chat.id, photo=fox_image_url)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

@bot.message_handler(func=lambda message: message.text == "Стикеры")
def stickers_url(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        bot.send_sticker(message.chat.id, sticker=Hand_em)
        bot.send_message(message.chat.id, f"{users[user_id]['name']}, Держи мой стикер пак:")
        bot.send_message(message.chat.id, "https://t.me/addstickers/Botlis8")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте /start для начала работы с ботом.")

bot.infinity_polling()