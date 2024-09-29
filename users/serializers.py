from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    """Сериализатор для моделей платежей"""
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей"""
    # Добавляю поле платежи, чтобы выводилась история платежей пользователя
    payment_history = PaymentSerializer(many=True, source='user')

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'profile_picture', 'payment_history')
