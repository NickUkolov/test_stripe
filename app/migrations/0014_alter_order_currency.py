# Generated by Django 4.1.7 on 2023-02-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'usd')], default='usd', max_length=3, null=True),
        ),
    ]
