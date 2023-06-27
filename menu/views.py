from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *


def get_menu_list(request):
    food_list = Food.objects.all()

    context = {
        'food_list': food_list,
    }
    return render(request, 'menu/menu_list.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_item': 0}

    context = {'items': items, 'order': order}
    return render(request, 'menu/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_item': 0}

    context = {'items': items, 'order': order}

    return render(request, 'menu/checkout.html', context)


def addItem(request, menu_id):
    """ Add a menu item to the cart """
    food = get_object_or_404(Food, id=menu_id)
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False
    )
    existing_order_item = OrderItem.objects.filter(order=order, product=food).first()
    print(existing_order_item)
    print("---")
    if existing_order_item:
        quantity = existing_order_item.quantity + 1
        order_item = OrderItem.objects.create(
            product=food, order=order, quantity=quantity
        )
    else:
        order_item = OrderItem.objects.create(
            product=food, order=order, quantity=1
        )
    return redirect(reverse('cart'))


@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productsId', productId)
    return JsonResponse('Item was added', safe=False)
