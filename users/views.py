from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework import filters

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer

from django_filters.rest_framework import DjangoFilterBackend


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

    # Добавляю фильтрацию по способу оплаты, оплаченному уроку или курсу
    filterset_fields = ('payment_method', 'paid_course', 'paid_lesson')

    # Добавляю сортировку по дате оплаты курса или урока
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date_of_payment',)
