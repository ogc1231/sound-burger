from django.contrib import admin
from .models import Burger
from .models import Side
from .models import Drink

admin.site.register(Burger)
admin.site.register(Side)
admin.site.register(Drink)
