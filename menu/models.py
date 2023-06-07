from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    addToOrder = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

