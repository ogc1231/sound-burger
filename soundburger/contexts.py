from menu.models import Order


def cart_items(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(
            customer=request.user, complete=False).first()
        if order is not None:
            cart_items = order.get_cart_items()
            return {"cart_items": cart_items}
        else:
            return {"cart_items": 0}
    else:
        return {"cart_items": 0}
