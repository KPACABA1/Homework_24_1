from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer


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


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к модели урок"""
        lesson = serializer.save()
        lesson.creator = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """Класс для вывода моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для вывода отдельной модели урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
