from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer


# Create your views here.
class CourseViewSet(ModelViewSet):
    """ViewSet для моделей курсов"""
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseSerializer


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания моделей уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


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
