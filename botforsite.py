import telebot

bot = telebot.TeleBot("1281831820:AAG_OW0oVU2xRc7jeU96wtnKJbsy3F33Rxo")

i = 0


@bot.message_handler(commands=['help', 'start'])
def send_keyboard(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("Информация о клиентах 🧑‍🤝‍🧑")  # Имена кнопок
    markup.add('Вывести отчёт 📗')  # Имена кнопок
    markup.add('Редактировать акции 📙')  # Имена кнопок
    bot.send_message(message.chat.id, text='wow', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    global i
    if i == 2:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Я очень голодный, когда привезут?")  # Имена кнопок
        bot.send_message(message.chat.id,
                         'Мы поторопили наших поваров. Они готовят также вкусно, но гораздо быстрее. Заказ будет у вас через 25 минут.',
                         reply_markup=markup)
    elif i == 0:
        bot.send_message(message.chat.id,'Заказ №34 принят.\n'
                                         '1. Вкусные блинчики - 1 шт.\n'
                                         '2. Малиновое варение - 2 шт.\n'
                                         'Сформировал ссылку на оплату в банке: https://yourbankforexamle.com/pay?pwn=12345\n'
                                         'Ожидаю информации о получении платежа и отправляю заказ на кухню.')
        i+=1
    elif i == 1:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Я очень голодный, когда привезут?")  # Имена кнопок
        bot.send_message(message.chat.id,'💚 Оплата осуществлена. Заказ №34 отправлен на кухню. Ожидайте время доставки в течении часа.', reply_markup=markup)
        i+=1
    elif i == 3:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # markup.add('Забронировать столик 🍴')  # Имена кнопок
        # markup.add('Отменить бронь ❌')  # Имена кнопок
        # markup.add('Обратный звонок 📱')  # Имена кнопок
        # markup.add('Акции 🤩', 'Помощь ℹ️')  # Имена кнопок
        markup.add("Информация о клиентах 🧑‍🤝‍🧑")  # Имена кнопок
        markup.add('Вывести отчёт 📗')  # Имена кнопок
        markup.add('Редактировать акции 📙')  # Имена кнопок
        #bot.send_message(message.chat.id,'Хорошо, забронировали для вас столик на 16:00, ждем вас! Мы скоро перезвоним с подтверждением.',reply_markup=markup)
        uis_pdf = open('files/' + '2020-31-08' + '.pdf', 'rb')
        bot.send_document(message.chat.id, uis_pdf, reply_markup=markup)
        uis_pdf.close()



if __name__ == '__main__':
    bot.polling()
