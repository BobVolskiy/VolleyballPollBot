import telebot
import time 
bot = telebot.TeleBot("1323796504:AAFa8HA_Q4fmhBEuk8C-46FUKr7UsIs5y0s")

cooldown = time.time()-60
@bot.message_handler(commands=['amongus'])
def amongus(message):
        global cooldown
        markdown = """
        *bold text*
        """
        GROUP_ID = message.chat.id
        name = message.from_user.first_name
        if time.time() - cooldown > 60:  
                bot.send_sticker(GROUP_ID,'CAACAgEAAxkBAAEBZwABX3cG_T-jgFo98C4-yCJntOVVLosAAjQAA54znB9AkrwUIJONCRsE')
                bot.send_message(GROUP_ID, '*'+name+'* призывает в *Among Us*!\n\nЗаходи в голосовой канал\nhttps://discord.gg/Z3rKddR',parse_mode= "Markdown")
                bot.send_sticker(GROUP_ID,'CAACAgEAAxkBAAEBZrxfdlrV2gUdNBh_sdOQ9nqOK9wlogACRgADnjOcH9odHIXtfgmvGwQ')
                cooldown=time.time()  

bot.polling() 
