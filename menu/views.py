from django.shortcuts import render
from .models import *


def get_menu_list(request):
    food_list = Food.objects.all()

    context = {
        'food_list': food_list,
    }
    return render(request, 'menu/menu_list.html', context)


def cart(request):
    context = {}
    return render(request, 'menu/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'menu/checkout.html', context)
