from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from users.permissions import ModeratorPermission, CreatorPermission


# Create your views here.
class CourseViewSet(ModelViewSet):
    """ViewSet для моделей курсов."""
    queryset = Course.objects.all()

    def get_serializer_class(self):
        """Метод для выбора другого сериализатора при создании модели."""
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к модели курс."""
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_permissions(self):
        """Метод для распределения прав доступа."""
        # Если действие на создание, то проверяем не является ли пользователь модератором
        if self.action == 'create':
            self.permission_classes = (~ModeratorPermission,)

        # Если действие на обновление или просмотр, то допускаем модератора или создателя курса
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (ModeratorPermission | CreatorPermission,)

        # Если действие на просмотр всех курсов, то допускаем только модератора
        elif self.action == 'list':
            self.permission_classes = (ModeratorPermission,)

        # Если действие на удаление, то проверяем не является ли пользователь модератором и является ли он создателем курса
        elif self.action == 'destroy':
            self.permission_classes = (~ModeratorPermission | CreatorPermission,)

        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания моделей уроков."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Доступ имеют все авторизованные пользователи, кроме модераторов
    permission_classes = (~ModeratorPermission, IsAuthenticated)

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к модели урок."""
        lesson = serializer.save()
        lesson.creator = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """Класс для вывода моделей уроков."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Доступ имеют только модераторы
    permission_classes = (ModeratorPermission, IsAuthenticated)


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для вывода отдельной модели урока."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Доступ имеют только модераторы или создатель урока
    permission_classes = (ModeratorPermission | CreatorPermission, IsAuthenticated)


class LessonUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей уроков."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Доступ имеют только модератор и создатель урока
    permission_classes = (ModeratorPermission | CreatorPermission, IsAuthenticated)


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей уроков."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Доступ имеет только создатель урока
    permission_classes = (~ModeratorPermission | CreatorPermission, IsAuthenticated)
