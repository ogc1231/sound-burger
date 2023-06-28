from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages

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

    context = {'items': items, 'order': order}
    return render(request, 'menu/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        if request.method == 'POST':
            print(request)
            order.complete = True
            order.save()
            messages.success(
                request, 'Order Complete, your food will be with you shortly')
            return redirect(reverse('home'))

    context = {'items': items, 'order': order}

    return render(request, 'menu/checkout.html', context)


def addItem(request, menu_id):
    food = get_object_or_404(Food, id=menu_id)
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False
    )
    existing_order_item = OrderItem.objects.filter(
        order=order, product=food).first()
    if existing_order_item is None:
        order_item = OrderItem.objects.create(
            product=food, order=order, quantity=1
        )
    else:
        existing_order_item.quantity += 1
        existing_order_item.save()
    messages.success(request, f'{food} added to cart')
    return redirect(reverse('cart'))


def deleteItem(request, menu_id):
    food = get_object_or_404(Food, id=menu_id)
    customer = request.user
    order = get_object_or_404(Order, customer=customer, complete=False)
    existing_order_item = OrderItem.objects.filter(
        order=order, product=food).first()
    if existing_order_item is not None:
        existing_order_item.delete()
        messages.error(request, f'{food} removed from cart')
    return redirect(reverse('cart'))
