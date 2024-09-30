from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    """Сериализатор для моделей платежей"""
    class Meta:
        model = Payment
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей пользователей"""
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'profile_picture', 'password')


class UserUpdateSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей, кроме создания"""
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'profile_picture')


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей, кроме создания и редактирования"""
    # Добавляю поле платежи, чтобы выводилась история платежей пользователя
    payment_history = PaymentSerializer(many=True, source='user')

    class Meta:
        model = User
        fields = ('id', 'email', 'phone_number', 'city', 'profile_picture', 'payment_history', 'password')
