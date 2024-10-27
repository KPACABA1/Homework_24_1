from celery import shared_task

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task
def sending_email_to_course_subscribers(email_course_subscribers):
    """Отложенная задача по отправке письма подписчикам курса, если курс обновился."""
    # Функция по отправке письма
    send_mail('Привет!', 'Курс на который ты подписан обновился', EMAIL_HOST_USER,
              email_course_subscribers)