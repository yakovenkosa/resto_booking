from django.conf import settings
from django.core.mail import send_mail


def send_messages(name, date_time, email):
    # Отправляем email-уведомление
    subject = "Ваше бронирование успешно создано"
    message = (
        f"Уважаемый(ая) {name},\n\n"
        f"Ваше бронирование на {date_time} успешно создано.\n"
        f"Спасибо за выбор нашего ресторана!\n\n"
        f"С уважением,\nКоманда ресторана Уютный домик"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Отправитель (указан в settings.py)
        [email],  # Получатель
        fail_silently=False,
    )
