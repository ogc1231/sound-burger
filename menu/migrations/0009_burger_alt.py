# Generated by Django 3.2.19 on 2023-06-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20230608_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='alt',
            field=models.CharField(default='placeholder', max_length=200),
        ),
    ]
