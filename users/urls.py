from django.urls import path

from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='lesson_list'),
    path('user/create/', UserCreateAPIView.as_view(), name='lesson_create'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='lesson_update'),
]
