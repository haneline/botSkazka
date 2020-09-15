from CodeGenerator import CodeGenerator
import telebot

bot = telebot.TeleBot("1377984156:AAEjNxPoNm8yOlqb0WR7fE62i8F0SaIp0mk")

@bot.message_handler(content_types=["text"])
def password_message(message):
    if message.text == "KQ3tn2qU11zZ9pm6GajE":
        Generator = CodeGenerator()
        bot.send_message(message.chat.id, Generator.code_add())

if __name__ == '__main__':
    bot.polling()

