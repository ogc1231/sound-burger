from django.contrib import admin
from .models import *

# admin.site.register(Customer)
# admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "food_type", "price", "is_public")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "complete")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    ordering = ("-order",)
