# Generated by Django 3.2.19 on 2023-06-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20230619_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='menu.Food')),
            ],
        ),
    ]
