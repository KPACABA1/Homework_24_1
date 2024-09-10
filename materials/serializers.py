from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'
