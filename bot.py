import telebot
import datab

b = telebot.TeleBot("5473254199:AAHpCgvLLnO00Q1G8Pcsyl7z2vmVjxdqPBE")

bd = datab.Base()

@b.message_handler(commands=["start"])
def s(mess):
    b.send_message(mess.chat.id, "Hello")


bd.loadLast()
bd.load("backup_1660320392")
b.infinity_polling()

