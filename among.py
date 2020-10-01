import telebot
import time 
bot = telebot.TeleBot("1323796504:AAFa8HA_Q4fmhBEuk8C-46FUKr7UsIs5y0s")

cooldown = time.time()-600
@bot.message_handler(commands=['amongus'])
def amongus(message):
        global cooldown
        GROUP_ID = message.chat.id
        name = message.from_user.first_name
        if time.time() - cooldown > 600:  
                bot.send_sticker(GROUP_ID,'CAACAgEAAxkBAAEBZrxfdlrV2gUdNBh_sdOQ9nqOK9wlogACRgADnjOcH9odHIXtfgmvGwQ')
                bot.send_message(GROUP_ID, name+' призывает всех поиграть в Among Us!\n\nЗаходи в голосовой канал, ссылка на игру будет в чате --> https://discord.gg/Z3rKddR')
                cooldown=time.time()
@bot.message_handler(commands=['cooldown'])
def send_welcome(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global cooldown
        if MEMBER_RANK=="Administrator" or message.from_user.first_name=="Боб":
                 cooldown=0
                 bot.send_message(GROUP_ID, 'Куллдаун сброшен')
      

bot.polling() 
