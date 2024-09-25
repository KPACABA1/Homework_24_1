from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson

import json

from django.core.serializers import serialize


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов, кроме создания"""
    # Добавляю дополнительное поле - количество уроков
    number_of_lessons = SerializerMethodField()

    # Добавляю поле вывода всей информации по урокам
    lesson_info = SerializerMethodField()

    def get_number_of_lessons(self, course):
        """Метод для получения дополнительного поля - количество уроков"""
        return course.course.count()

    def get_lesson_info(self, course):
        """Метод для получения всей информации по урокам"""
        # Получаю все уроки, связанные с курсом
        lesson = Lesson.objects.filter(course=course)
        # Перевожу все полученные модели в формат JSON
        json_lesson = json.loads(serialize('json', lesson))
        return json_lesson

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'number_of_lessons', 'lesson_info')


class CourseCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей курсов"""
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description')
