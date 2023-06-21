from django.shortcuts import render
from django.views import View
from .models import Food, OrderModel


def get_menu_list(request):
    food_list = Food.objects.all()

    context = {
        'food_list': food_list,
    }
    return render(request, 'menu/menu_list.html', context)


class Order(View):
    def get_order(self, request, *args, **kwargs):
        burgers = Food.objects.filter(category__name__contains='Burger')
        sides = Food.objects.filter(category__name__contains='Side')
        drinks = Food.objects.filter(category__name__contains='Drink')

        context = {
            'burgers': burgers,
            'sides': sides,
            'drinks': drinks,
        }

        return render(request, 'menu/order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = Food.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            order_items['items'].append(item_data)

            price = 0
            items_id = []

            for item in order_items['items']:
                price += item['price']
                item.ids.append(item['id'])

            order = OrderModel.objects.create(price=price)
            order.items.add(*item_id)

            context = {
                'items': order_items['items'],
                'price': price,
            }

            return (render(request, 'menu/order_confirmation.html'))

