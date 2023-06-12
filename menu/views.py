from django.shortcuts import render
from django.views import generic
from .models import Burger
from .models import Side
from .models import Drink


class BurgerList(generic.ListView):
    model = Burger()
    queryset = Burger.objects.filter(status=1).order_by('created')
    template_name = 'menu.html'


class SideList(generic.ListView):
    model = Side()
    queryset = Side.objects.filter(status=1).order_by('created')
    template_name = 'menu.html'
    

class DrinkList(generic.ListView):
    model = Drink()
    queryset = Drink.objects.filter(status=1).order_by('created')
    template_name = 'menu.html'
