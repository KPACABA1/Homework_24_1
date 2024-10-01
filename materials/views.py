from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from users.permissions import ModeratorPermission


# Create your views here.
class CourseViewSet(ModelViewSet):
    """ViewSet для моделей курсов"""
    queryset = Course.objects.all()

    def get_serializer_class(self):
        """Метод для выбора другого сериализатора при создании модели"""
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к модели курс"""
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_permissions(self):
        """Метод для распределения прав доступа"""
        # Если действие на создание и удаление, то проверяем не является ли пользователь модератором
        if self.action in ['create', 'destroy']:
            self.permission_classes = (~ModeratorPermission,)
        # Если действие на обновление или просмотр, то допускаем модератора
        elif self.action in ['list', 'update', 'retrieve']:
            self.permission_classes = (ModeratorPermission,)
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~ModeratorPermission,)

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к модели урок"""
        lesson = serializer.save()
        lesson.creator = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """Класс для вывода моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (ModeratorPermission,)


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для вывода отдельной модели урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (ModeratorPermission,)


class LessonUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (ModeratorPermission,)


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~ModeratorPermission,)
