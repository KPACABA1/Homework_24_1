from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)
    phone_number = PhoneNumberField(blank=True, verbose_name='Номер телефона', null=True)
    city = models.CharField(max_length=20, verbose_name='Город', null=True, blank=True)
    profile_picture = models.ImageField(verbose_name='Аватарка', null=True, blank=True, upload_to="users/")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Модель платежа"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user')
    date_of_payment = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Оплаченный курс',
                                    related_name='paid_course', null=True, blank=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок',
                                    related_name='paid_lesson', null=True, blank=True)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.BooleanField(default=True, verbose_name='Тип оплаты(если True - безнал, Если False - '
                                                                    'наличка)')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'Пользователь - {self.user}, оплатил {self.payment_amount}'

