# Generated by Django 4.1.7 on 2023-02-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, max_length=128),
        ),
    ]
