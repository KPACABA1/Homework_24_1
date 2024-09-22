from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов"""
    # Добавляю дополнительное поле - количество уроков
    number_of_lessons = SerializerMethodField()

    # Поле уроки переделываю так, чтобы выводилась полная информация по ним
    lesson_list = LessonSerializer(many=True)

    def get_number_of_lessons(self, course):
        """Метод для получения дополнительного поля - количество уроков"""
        return course.lesson.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'number_of_lessons', 'lesson_list')
