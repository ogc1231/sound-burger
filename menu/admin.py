from django.contrib import admin
from .models import *


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "food_type", "price", "is_public")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "id", "complete")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    ordering = ("-order",)
