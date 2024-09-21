from django.urls import path

from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, PaymentListAPIView, PaymentCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # Урылы для пользователей
    path('user/', UserListAPIView.as_view(), name='lesson_list'),
    path('user/create/', UserCreateAPIView.as_view(), name='lesson_create'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='lesson_update'),

    # Урлы для платежей
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
]
