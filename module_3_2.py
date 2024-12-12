def send_email(messege=(), recipient=(), sender="university.help@gmail.com"):
    if  "@" not in recipient or "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    address = (".com", ".ru", ".net")
    if not recipient.endswith(address) or not sender.endswith(address):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print(" Нельзя отправить письмо самому себе! ")
        return
    if sender== ("university.help@gmail.com"):
        print (f" Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        return


send_email(" Э родственник , ты мне РУБЛЬ должен!", "a2031279@yandex.ru")


# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
