from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
#import send_mail

import os
import smtplib
import imghdr
from email.message import EmailMessage

TG_TOKEN = "1242448847:AAH_bKNPvJgN_QvK1qDJ1_V1WTpezaPV5ow"


def send_mails(mail_To):
    #EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    #EMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
    EMAIL_ADDRESS = "gannaivanchenko.forpeople@gmail.com"
    EMAIL_PASSWORD = "dxjivieeucueuhcc"


    msg = EmailMessage()
    msg['Subject'] = 'Завтрак 03.09.2020'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = mail_To
    msg.set_content('Прекрасного времени суток,\n' 
                    'Вот ссылка на закрытый видеоурок:\n' 
                    'https://youtu.be/5CjrsJSsE64\n'
                    'Вот ссылка на ссылка на упражнение:\n'
                    'https://youtu.be/zD-TQT1WNGE\n'                    
'Видео с завтрака 03.09.2020 на тему «Сила Рода» с подробным описанием практики по проработке. Видео по ссылке являться эксклюзивным и не находиться в свободном доступе.\n' 
'Хорошего настроения и приятного просмотра.\n' 
'С уважением,\n'
'Ганна\n')

    #with open('','rb') as f:
     #   file_data = f.read()
      #  file_type = imghdr.what(f.name)
      #  file_name = f.name

    #msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Eto uchebnyj Bot\n"
        "Eto uchebnyj Bot\n"
        "Eto uchebnyj Bot\n",
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Privet! otpravj mne shto nibud",
    )

def do_echo(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Mail send to "+text,
    )
    send_mails(text)


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )

    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
