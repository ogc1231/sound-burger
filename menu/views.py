from django.shortcuts import render
from .models import *


def get_menu_list(request):
    food_list = Food.objects.all()

    context = {
        'food_list': food_list,
    }
    return render(request, 'menu/menu_list.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'menu/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'menu/checkout.html', context)
