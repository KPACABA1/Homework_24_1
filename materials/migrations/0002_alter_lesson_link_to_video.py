# Generated by Django 4.2.2 on 2024-09-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="link_to_video",
            field=models.TextField(
                blank=True, null=True, verbose_name="Ссылка на видео"
            ),
        ),
    ]
