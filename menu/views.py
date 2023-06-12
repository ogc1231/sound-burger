from django.shortcuts import render
from .models import Burger
from .models import Side
from .models import Drink


def get_menu_list(request):
    burgers = Burger.objects.all()
    sides = Side.objects.all()
    drinks = Drink.objects.all()
    context = {
        'burgers': burgers,
        'sides': sides,
        'drinks': drinks
    }
    return render(request, 'menu/menu_list.html', context)
