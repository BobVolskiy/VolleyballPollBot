import telebot
import datetime
import time  
import locale
timing = time.time()-45000 
bot = telebot.TeleBot("1381051273:AAHATq_xhk-piS6dU2Txv2P6POGor5pNoOs")
options = ["Да", "50/50", "Нет"]
locale.setlocale(locale.LC_ALL, "ru") 


def rtoday(): 
        date_today=datetime.date.today() + datetime.timedelta(days=0) 
        global question_today
        question_today = "Волейбол сегодня "+str(date_today.day)+"."+str(date_today.strftime("%m"))+" ("+date_today.strftime("%A")+")?"

def rtomorrow():
        date_tomorrow=datetime.date.today() + datetime.timedelta(days=1) 
        global question_tomorrow
        question_tomorrow = "Волейбол завтра "+str(date_tomorrow.day)+"."+str(date_tomorrow.strftime("%m"))+" ("+date_tomorrow.strftime("%A")+")?"

def rdayafter(): 
        date_dayafter=datetime.date.today() + datetime.timedelta(days=2) 
        global question_dayafter
        question_dayafter = "Волейбол послезавтра "+str(date_dayafter.day)+"."+str(date_dayafter.strftime("%m"))+" ("+date_dayafter.strftime("%A")+")?" 

@bot.message_handler(commands=['cooldown'])
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

@bot.message_handler(commands=['today'])
def volley_today(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        rtoday()
        if time.time() - timing > 43200:  
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_today+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False) 
                        bot.pin_chat_message(GROUP_ID, message.message_id+1)
                        timing = time.time() 
                        pollnumber = message.message_id+1 
        bot.delete_message(GROUP_ID, message.message_id)  

@bot.message_handler(commands=['tomorrow'])
def volley_tomorrow(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        rtomorrow()
        if time.time() - timing > 43200:
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_tomorrow+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False)
                        bot.pin_chat_message(GROUP_ID, message.message_id+1)
                        timing = time.time()
                        pollnumber = message.message_id+1
        bot.delete_message(GROUP_ID, message.message_id)  

@bot.message_handler(commands=['dayafter'])
def volley_dayafter(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing
        global pollnumber
        rdayafter()
        if time.time() - timing > 43200:
                if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                        bot.send_poll(chat_id=GROUP_ID, question=question_dayafter+' - '+bot.get_chat_member(GROUP_ID, MEMBER_ID).user.first_name, options = options, is_anonymous=False)
                        bot.pin_chat_message(GROUP_ID, message.message_id+1)
                        timing = time.time()
                        pollnumber = message.message_id+1
        bot.delete_message(GROUP_ID, message.message_id)  
                
bot.polling() 
