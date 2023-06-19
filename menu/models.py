from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Food(models.Model):
    TYPES = (('burger', 'Burger'), ('side', 'Side'), ('drink', 'Drink'))
    food_type = models.CharField(
        choices=TYPES, max_length=10, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField()
    price = models.FloatField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    item_image = CloudinaryField('image', default='placeholder')
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
