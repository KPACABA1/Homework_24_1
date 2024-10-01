from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для пользователей"""
    list_display = ('id', 'email')
