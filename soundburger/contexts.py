from django.shortcuts import get_object_or_404
from menu.models import Order


# get total number of cart items
def cart_items(request):
    order = get_object_or_404(Order, customer=request.user, complete=False)
    cart_items = order.get_cart_items()
    return {"cart_items": cart_items}
