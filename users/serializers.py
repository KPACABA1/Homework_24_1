from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей уроков"""
    class Meta:
        model = User
        # exclude = ('password1', 'password2')
        fields = '__all__'g
