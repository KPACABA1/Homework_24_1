# Generated by Django 4.2.2 on 2024-09-10 06:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Город"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="Номер телефона",
            ),
        ),
    ]
