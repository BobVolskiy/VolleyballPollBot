import telebot

bot = telebot.TeleBot("1312025506:AAF5K4xuPAhocTp_QSqL2imsFmf03JyRR_A")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()



import datetime
import time  
timing = time.time()-45000 
pollnumber=0
bot = telebot.TeleBot('1312025506:AAF5K4xuPAhocTp_QSqL2imsFmf03JyRR_A')

date_today=datetime.date.today() + datetime.timedelta(days=0) 
date_tomorrow=datetime.date.today() + datetime.timedelta(days=1) 
date_dayafter=datetime.date.today() + datetime.timedelta(days=2) 
question_today = "Волейбол "+str(date_today.day)+"."+str(date_today.strftime("%m"))+" ("+date_today.strftime("%a")+")?"  
question_tomorrow = "Волейбол "+str(date_tomorrow.day)+"."+str(date_tomorrow.strftime("%m"))+" ("+date_tomorrow.strftime("%a")+")?" 
question_dayafter = "Волейбол "+str(date_dayafter.day)+"."+str(date_dayafter.strftime("%m"))+" ("+date_dayafter.strftime("%a")+")?" 
options = ["Да", "50/50", "Нет"]



@bot.message_handler(commands=['dellpoll']) 
def send_welcome(message): 
        MEMBER_ID = message.from_user.id  
        GROUP_ID = message.chat.id 
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status 
        global pollnumber 
        if MEMBER_RANK=="creator": 
                if pollnumber!=0: 
                        bot.delete_message(GROUP_ID, pollnumber) 
                        pollnumber=0
        bot.delete_message(GROUP_ID, message.message_id) 



@bot.message_handler(commands=['delltime'])
def send_welcome(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        if MEMBER_RANK=="creator":
                global timing 
                if timing>600: 
                        timing=0 
                        bot.send_message(GROUP_ID, 'Куллдаун сброшен')
        bot.delete_message(GROUP_ID, message.message_id)
            

@bot.message_handler(commands=['volley_today'])
def send_welcome(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        if time.time() - timing > 43200:  
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_today+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False) 
                        timing = time.time() 
                        pollnumber = message.message_id+1 
                        bot.delete_message(GROUP_ID, message.message_id)
        else:
                bot.delete_message(GROUP_ID, message.message_id)


@bot.message_handler(commands=['volley_tomorrow'])
def send_welcome(message):
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


@bot.message_handler(commands=['volley_dayafter'])
def send_welcome(message):
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
