from django.db import models

# Create your models here.
class Course(models.Model):
    """Модель курса"""
    title = models.CharField(max_length=35, verbose_name='название')
    preview = models.ImageField(verbose_name='Превью(изображение)', null=True, blank=True, upload_to='materials/course')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=35, verbose_name='название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(verbose_name='Превью(изображение)', null=True, blank=True, upload_to='materials/lesson')
    link_to_video = models.TextField(verbose_name='Ссылка на видео', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс',
                                    related_name='course', null=True, blank=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}'
