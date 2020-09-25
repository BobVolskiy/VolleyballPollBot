import telebot # модуль телеграм бота
import datetime # модуль даты
import locale # модуль языка1
import time     # модуль времени (отсчёт с 1940 вроде года) 
timing = time.time()-45000 # Задаем время и отматываем его назад, чтобі можно было согдать голосование
pollnumber=0
locale.setlocale(locale.LC_ALL, "ru") # задаем Русский язык для вывода времени на русском
bot = telebot.TeleBot('1312025506:AAF5K4xuPAhocTp_QSqL2imsFmf03JyRR_A') # Инициализация телеграм бота по коду

date_today=datetime.date.today() + datetime.timedelta(days=0) # сегодняшняя дата
date_tomorrow=datetime.date.today() + datetime.timedelta(days=1) # завтрашняя дата
date_dayafter=datetime.date.today() + datetime.timedelta(days=2) # послезавтрашняя дата

question_today = "Волейбол "+str(date_today.day)+"."+str(date_today.strftime("%m"))+" ("+date_today.strftime("%a")+")?"  # текст опроса на сегодня
question_tomorrow = "Волейбол "+str(date_tomorrow.day)+"."+str(date_tomorrow.strftime("%m"))+" ("+date_tomorrow.strftime("%a")+")?" # текст опроса на завтра
question_dayafter = "Волейбол "+str(date_dayafter.day)+"."+str(date_dayafter.strftime("%m"))+" ("+date_dayafter.strftime("%a")+")?" # текст опроса на послезавтра
options = ["Да", "50/50", "Нет"]


# удаление предыдущего голосования
@bot.message_handler(commands=['dellpoll']) # реакция на команду
def dellpoll(message):  # функция команды
        MEMBER_ID = message.from_user.id   # Достаем ID отправителя
        GROUP_ID = message.chat.id # Достаем ID группы, где отправили
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status # Достеаем уровень крутости отправителя
        global pollnumber # Достаем номер предыдущего голосование. Если 0 - значит оно не создано
        if MEMBER_RANK=="creator": # Проверка крутости отправителя
                if pollnumber!=0: # Голосование создано?
                        bot.delete_message(GROUP_ID, pollnumber) # Удаление голосования
                        pollnumber=0
        bot.delete_message(GROUP_ID, message.message_id) # Удаление посланной команды


# сброс времени
@bot.message_handler(commands=['delltime'])
def delltime(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        if MEMBER_RANK=="creator":
                global timing # Достаем время
                if timing>600: # Проверка куллдауна куллдауна ))))
                        timing=0 # Сброс Куллдауна
                        bot.send_message(GROUP_ID, 'Куллдаун сброшен')
        bot.delete_message(GROUP_ID, message.message_id)
            

@bot.message_handler(commands=['volley_today']) # голосование на сегодня
def volley_today(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        if time.time() - timing > 43200:  # Куллдаун в 12 часов
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_today+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False) # Отправка голосования
                        timing = time.time() # Запускаем куллдаун
                        pollnumber = message.message_id+1 # Выставляем номер голосования, если вдруг надо будет его удалить
                        bot.delete_message(GROUP_ID, message.message_id)
        else:
                bot.delete_message(GROUP_ID, message.message_id)


@bot.message_handler(commands=['volley_tomorrow']) # голосование на завтра
def volley_tomorrow(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        if time.time() - timing > 43200:
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_tomorrow+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False)
                        timing = time.time()
                        pollnumber = message.message_id+1
                        bot.delete_message(GROUP_ID, message.message_id)
        else:
                bot.delete_message(GROUP_ID, message.message_id)


@bot.message_handler(commands=['volley_dayafter']) # голосование на послезавтра
def volley_dayafter(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        if time.time() - timing > 43200:
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_dayafter+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False)
                        timing = time.time()
                        pollnumber = message.message_id+1
                        bot.delete_message(GROUP_ID, message.message_id)
        else:
                bot.delete_message(GROUP_ID, message.message_id)


bot.polling() # я не знаю что это но без этого бот не выводит сообщения
