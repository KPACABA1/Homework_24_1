# Generated by Django 5.1.1 on 2024-10-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_payment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Статус оплаты"
            ),
        ),
    ]
