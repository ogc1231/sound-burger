# Generated by Django 3.2.19 on 2023-06-25 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
