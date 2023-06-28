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
    """ Add a menu item to the cart """
    food = get_object_or_404(Food, id=menu_id)  # the food item
    customer = request.user  # the user
    # create a new order for this user, if none found
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False
    )
    # check for an existing food item on this user's specific order
    existing_order_item = OrderItem.objects.filter(
        order=order, product=food).first()
    # if no matching food item, create a new instance of the order-item
    if existing_order_item is None:
        order_item = OrderItem.objects.create(
            product=food, order=order, quantity=1
        )
    else:
        # existing food on this order was found, increment the quantity by +1
        existing_order_item.quantity += 1
        # save the changes to the DB
        existing_order_item.save()
    messages.success(request, f'{food} added to cart')
    return redirect(reverse('cart'))


def deleteItem(request, menu_id):
    """ Removes an item from user's cart """
    food = get_object_or_404(Food, id=menu_id)  # the food item
    customer = request.user  # the user
    # get the user's non-completed order
    order = get_object_or_404(Order, customer=customer, complete=False)
    # get the existing food item on this user's specific order
    existing_order_item = OrderItem.objects.filter(
        order=order, product=food).first()
    # if no matching food item, create a new instance of the order-item
    if existing_order_item is not None:
        # existing food on this order was found, delete it
        existing_order_item.delete()
        messages.error(request, f'{food} removed from cart')
    return redirect(reverse('cart'))
