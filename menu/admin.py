from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "food_type", "price", "is_public")
