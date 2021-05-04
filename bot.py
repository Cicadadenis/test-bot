import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

Button1 = types.KeyboardButton("Подписаться✅")
Button2 = types.KeyboardButton("Отписаться🚫")
Button3 = types.KeyboardButton("Написать в тех.поддержку\nпо любым вопросам🕹⚒💵")
Button4 = types.KeyboardButton("STOP🚫")
Button5 = types.KeyboardButton("Admin")
Button6 = types.KeyboardButton("Включить бота✅")
Button7 = types.KeyboardButton('Ответ подписчику✏️")
Button8 = types.KeyboardButton("Удаление сообщений🗑")
Button9 = types.KeyboardButton("ПЕРЕЗАГРУЗКА 🔁")
Button10 = types.KeyboardButton("Написать ВСЕМ✏️")
Button11 = types.KeyboardButton("СТАТИСТИКА📊")
Button12 = types.KeyboardButton("Чем поможет этот бот?🌟")
Button13 = types.KeyboardButton("РАЗБОР ВАШЕГО ПРОФИЛЯ🤩")
Button14 = types.KeyboardButton("ПОЛУЧИТЬ КУРС💎")

stop = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Button4)
start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Button2, Button1).row(Button14).row(Button13).row(Button12).row(Button3)
adminon = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Button9, Button7).row(Button8).row(Button10).row(Button11)



@bot.message_handler(commands=['start'])
def welcome(message):
	if message.chat.type == 'private':
		sti = open('static/welcome.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)

	# клавиатура
       
	types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.InlineKeyboardButton("🎲 Рандомное число", callback_data='dad')
	item2 = types.InlineKeyboardButton("😊 Как дела?", callback_data='pop')

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'dad':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'pop':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
				reply_markup=None)

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Рандомное число':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
				reply_markup=None)

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)
