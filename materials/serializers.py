from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков."""
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов, кроме создания."""
    # Добавляю дополнительное поле - количество уроков
    number_of_lessons = SerializerMethodField()

    lesson_info = LessonSerializer(many=True, source='course')

    def get_number_of_lessons(self, course):
        """Метод для получения дополнительного поля - количество уроков."""
        return course.course.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'number_of_lessons', 'lesson_info', 'creator')


class CourseCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей курсов."""
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description')
