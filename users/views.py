from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


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


class PaymentCreateAPIView(CreateAPIView):
    """Класс для создания платежей пользователей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    """Класс для вывода всех платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
