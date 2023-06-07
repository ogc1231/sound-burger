from django.db import models


class Burger(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Side(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Drink(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

