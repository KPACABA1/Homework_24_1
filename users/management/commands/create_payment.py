from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    """Команда для создания 2 платежей(1 платеж за курс, 2 за урок)"""
    def handle(self, *args, **options):
        # Создаю платеж за курс
        payment_course = Payment.objects.create(user=User.objects.get(pk=1), date_of_payment='2024-09-21',
                                                paid_course=Course.objects.get(pk=1), payment_amount=200000,
                                                payment_method=True)
        payment_course.save()

        # Создаю платеж за урок
        payment_lesson = Payment.objects.create(user=User.objects.get(pk=1), date_of_payment='2024-09-21',
                                                paid_lesson=Lesson.objects.get(pk=1), payment_amount=15000,
                                                payment_method=True)
        payment_lesson.save()
