# Generated by Django 3.2.19 on 2023-06-07 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20230607_1033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu_item',
            new_name='Menu',
        ),
    ]
