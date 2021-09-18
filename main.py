import telebot
import recursos
import os

bot = telebot.TeleBot(os.environ['SOFTGRAF_BOT_TOKEN'], parse_mode=None)
canal = os.environ['SOFTGRAF_ID_CANAL']
saudacao = recursos.saudacao

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def boas_vindas(message):
    if(message.chat.id == canal):
        bot.send_message(canal,saudacao)

@bot.message_handler(commands=['start'])
def enviar_saudacao(message):
    bot.send_message(message.chat.id,saudacao)

bot.polling()