from CodeGenerator import CodeGenerator
import telebot
bot = telebot.TeleBot("1310630322:AAHk7aNFpZc4g2u0h_OC5J34XznoeTFJY88")

CodeGen = CodeGenerator()


@bot.message_handler(commands=['start'])
def start_handler(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет, я пока умею просто проверять коды. Попробуешь? Введи свой код.')


@bot.message_handler(content_types=["text"])
def text_handler(message):
    print(message)
    if CodeGen.code_use(message.text) is True:
        bot.send_message(message.chat.id, "Ты великолепен, твой код работает!")
    else:
        bot.send_message(message.chat.id, "Упс, ошибочка, код использован или не существует")


bot.polling()
