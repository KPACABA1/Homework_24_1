from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    """Класс для создания моделей пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """Класс для вывода всех моделей пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
