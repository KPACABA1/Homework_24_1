from django.contrib import admin

from materials.models import Subscription


# Register your models here.
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Админка для подписок"""
    list_display = ('id', 'user', 'course')
