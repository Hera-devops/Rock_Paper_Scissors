import telebot
from telebot import types
import random

rnum = 0
tools = ['rock', 'paper', 'scissor']
bot = telebot.TeleBot('TOKEN', parse_mode=None)

markup = types.ReplyKeyboardMarkup(row_width=2)
rock = types.KeyboardButton('ROCK')
papper = types.KeyboardButton('PAPER')
scissor = types.KeyboardButton('SCISSOR')
markup.add(rock, papper, scissor)

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
	bot.send_message(message.chat.id, 'To start the game\nTypes /play')

@bot.message_handler(commands=['play'])
def play(message):
	bot.send_message(message.chat.id, 'GAME STARTED',reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def procces(message):
	if message.text.lower() in tools:
		rnum = random.randint(0,2)
		bot.send_message(message.chat.id, tools[rnum].upper())
		if message.text.lower() == tools[rnum]:
			bot.send_message(message.chat.id, '___DRAW___')
		elif (message.text.lower() == 'rock' and tools[rnum] == 'paper') or (message.text.lower() == 'paper' and tools[rnum] == 'scissor') or (message.text.lower() == 'scissor' and tools[rnum] == 'rock'):
			bot.send_message(message.chat.id, '___I WON___')
		elif (message.text.lower() == 'paper' and tools[rnum] == 'rock') or (message.text.lower() == 'scissor' and tools[rnum] == 'paper') or (message.text.lower() == 'rock' and tools[rnum] == 'scissor'):
			bot.send_message(message.chat.id, '___YOU WON___')
	else:
		bot.send_message(message.chat.id, message.text.upper())

bot.polling()

