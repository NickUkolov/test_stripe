# Generated by Django 4.1.7 on 2023-02-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_order_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'usd')], max_length=3, null=True),
        ),
    ]