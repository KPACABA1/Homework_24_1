from django.urls import path

from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, PaymentListAPIView, PaymentCreateAPIView, \
    UserRetrieveAPIView, UserDestroyAPIView
from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny

app_name = UsersConfig.name

urlpatterns = [
    # Урылы для пользователей
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/register/', UserCreateAPIView.as_view(), name='register'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/<int:pk>/retrieve/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('user/<int:pk>/destroy/', UserDestroyAPIView.as_view(), name='user_destroy'),

    # Урлы для платежей
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),

    # Урлы для ACCESS и REFRESH токенов
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]
