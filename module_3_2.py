def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if (recipient.find('@') < 0 or sender.find('@') < 0
            or (recipient[-4:len(recipient)] != '.com' and recipient[-3:len(recipient)] != '.ru'
            and recipient[-4:len(recipient)] != '.net')
            or (sender[-4:len(sender)] != '.com' and sender[-3:len(sender)] != '.ru'
            and sender[-4:len(sender)] != '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif (recipient == sender):
        print('Нельзя отправить письмо самому себе!')
    elif (sender == 'university.help@gmail.com'):
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '
              f'Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')