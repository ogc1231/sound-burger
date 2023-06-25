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


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Food, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    eircode = models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address