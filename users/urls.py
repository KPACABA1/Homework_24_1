from django.urls import path

from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, PaymentListAPIView, PaymentCreateAPIView, \
    UserRetrieveAPIView, UserDestroyAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # Урылы для пользователей
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/<int:pk>/retrieve/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('user/<int:pk>/destroy/', UserDestroyAPIView.as_view(), name='user_destroy'),

    # Урлы для платежей
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
]
