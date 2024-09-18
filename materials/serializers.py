from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов"""
    # Добавляю дополнительное поле - количество уроков
    number_of_lessons = SerializerMethodField()

    def get_number_of_lessons(self, course):
        """Метод для получения дополнительного поля - количество уроков"""
        return course.lesson.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lesson', 'number_of_lessons')


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'
