from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_links


class LessonSerializer(ModelSerializer):
    """Сериализатор для моделей уроков."""
    # Ввожу проверку на то, что ссылка из YouTube
    link_to_video = CharField(validators=[validate_links])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Сериализатор для моделей курсов, кроме создания."""
    # Добавляю дополнительное поле - количество уроков
    number_of_lessons = SerializerMethodField()

    # Добавляю дополнительное поле, чтобы выводилось подписан ли текущий пользователь курс или нет
    subscription = SerializerMethodField()

    lesson_info = LessonSerializer(many=True, source='course')

    def get_number_of_lessons(self, course):
        """Метод для получения дополнительного поля - количество уроков."""
        return course.course.count()

    def get_subscription(self, course):
        """Метод для вывода подписан ли текущий пользователь курс или нет."""
        try:
            # Пытаюсь получить подписку на курс
            subscription = Subscription.objects.get(user=course.creator, course=course)
            return 'Подписка активна'

        except Subscription.DoesNotExist:
            # Если не получилось найти подписку, то сообщаю об этом пользователю
            return 'Подписка не активна'

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'number_of_lessons', 'lesson_info', 'creator', 'subscription')


class CourseCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей курсов."""
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description')


class SubscriptionSerializer(ModelSerializer):
    """Сериализатор для подписок на курс."""

    class Meta:
        model = Subscription
        fields = '__all__'
