# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)

def start(update, context):
	''' START '''
	context.bot.send_message(update.message.chat_id, "Bienvenido")

def main():
	TOKEN=""
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activará nuestro bot.
	dp.add_handler(CommandHandler('start',	start))

	# Inicia el bot
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()