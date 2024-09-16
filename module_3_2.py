b = 0


def count_calls():
    global b
    b += 1
    return b


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    count_calls()
    a = True
    for k in range(0, b):
        if a:

            for i in range(0, len(recipient)):
                if recipient[i] == '@' or recipient[-4:] == ".com" or recipient[-3:] == ".ru" or recipient[
                                                                                                 -4:] == ".net":
                    continue
                else:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                    a = False
                    break

            for j in range(0, len(sender)):
                if sender[j] == '@' or sender[-4:] == ".com" or sender[-3:] == ".ru" or sender[-4:] == ".net":
                    continue
                else:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                    a = False
                    break

        if a:
            if sender == recipient:
                print("Нельзя отправить письмо самому себе!")
            elif sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
