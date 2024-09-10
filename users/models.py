from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
