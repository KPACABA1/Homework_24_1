# Generated by Django 5.1.1 on 2024-10-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="id_session",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Id сессии"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
    ]
