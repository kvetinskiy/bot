import telepot, time, subprocess, ReplyKeyboardRemove



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/help' in command:
            p = " [?]Помощь[?]\n  Наши продукты  - /price \n Наши контакты и информация о нас - /info \n Использование телеграм ботов в бизнесе - /buis"
            bot.sendMessage(chat_id, p)

        if  '/price' in command:#В кавычках команда которую мы будем писать в телеграмм.
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = "Создание бота - 10000р\nАдминистрирование - 1000р"#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, p)#А это ответ бота в чат.

        if  '/info' in command:
            p = "Тут будет информация о нас и наши контакты!!1!"
            bot.sendMessage(chat_id, p)

        if  '/buis' in command:
            p = "Тут будет информация о ботах в бизнесе и т.д."
            bot.sendMessage(chat_id, p)



bot = telepot.Bot('677177030:AAGSZb4ES82-MX2-3VHtAHbny_0KxGTwiiM')#Вместо иксов пишем ваш токен
bot.message_loop(handle)

while 1:
    time.sleep(20)
