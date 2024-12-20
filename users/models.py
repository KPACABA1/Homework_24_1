import materials.models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    """Модель пользователя."""
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
    """Модель платежа."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user',
                             null=True, blank=True)
    date_of_payment = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(materials.models.Course, on_delete=models.SET_NULL, verbose_name='Оплаченный курс',
                                    related_name='paid_course', null=True, blank=True)
    paid_lesson = models.ForeignKey(materials.models.Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок',
                                    related_name='paid_lesson', null=True, blank=True)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=37,
                                      choices=(('cash', 'Наличные'), ('non-cash', 'Безнал'), ('cash and non-cash', 'Частично наличные и частично безнал')),
                                      verbose_name='Способ оплаты(3 на выбор)')
    id_session = models.CharField(max_length=255, null=True, blank=True, verbose_name='Id сессии')
    payment_link = models.URLField(max_length=400, null=True, blank=True, verbose_name='Ссылка на оплату')
    payment_status = models.CharField(max_length=100, null=True, blank=True, verbose_name='Статус оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'Пользователь - {self.user}, оплатил {self.payment_amount}'
