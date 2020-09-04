import os
import smtplib
import imghdr
from email.message import EmailMessage

def send_mails(mail_To):
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = 'Завтрак 03.09.2020'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = mail_To
    msg.set_content('Прекрасного времени суток,\n' 
                    'Вот ссылка на закрытый ютуб-канал:\n' 
                    'https://youtu.be/DUaEfdcq_II\n'
'Видео с завтрака 27.08.2020 на тему проработки лимитов и ограничений, с подробным описанием упражнений. Видео по ссылке являться эксклюзивным и не находиться в свободном доступе.\n' 
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