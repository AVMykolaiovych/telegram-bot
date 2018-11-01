import telebot
from telebot import types
from telebot.types import Message

TOKEN = '530405139:AAEX64Ux6wvfyAZdg3KL67124nYcuoNMPM8'

bot = telebot.TeleBot(TOKEN)

User = set()


@bot.message_handler(commands=['start'])
def message_handler(message: Message):
    bot.reply_to(message, 'Start command reply')


@bot.message_handler(commands=['help'])
def message_handler(message: Message):
    bot.reply_to(message, 'Help command reply')


@bot.message_handler(content_types=['text'])
def message_handler(message: Message):
    User.add(message.from_user.id)
    bot.reply_to(message, 'Message reply')


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Like", callback_data="data"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Inline message"),
        reply_markup=keyboard
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


bot.polling()
