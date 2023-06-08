from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Burger(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    item_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Side(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    item_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    item_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
