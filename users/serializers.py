import json

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.core.serializers import serialize

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    """Сериализатор для моделей платежей"""
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей"""
    # Добавляю поле платежи, чтобы выводилась история платежей пользователя
    payment_history = SerializerMethodField()

    def get_payment_history(self, user):
        """Метод для получения поля история платежей"""
        # Получаю все платежи, связанные с пользователем
        payment = Payment.objects.filter(user=user)
        # Перевожу все полученные модели в формат JSON
        json_payment = json.loads(serialize('json', payment))
        return json_payment

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'profile_picture', 'payment_history')
