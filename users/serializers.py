from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей"""
    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    """Сериализатор для моделей платежей"""
    class Meta:
        model = Payment
        fields = '__all__'
