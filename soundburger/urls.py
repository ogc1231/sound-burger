from django.contrib import admin
from django.urls import path, include
from menu.views import get_menu_list, cart, checkout, addItem, deleteItem
from reviews.views import (
    get_review_list, add_review, edit_review, delete_review)
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('menu/', get_menu_list, name='get_menu_list'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_item/<menu_id>/', addItem, name='add_item'),
    path('delete_item/<menu_id>/', deleteItem, name='delete_item'),
    path('reviews/', get_review_list, name='get_review_list'),
    path('add/', add_review, name='add_review'),
    path('edit/<review_id>', edit_review, name='edit_review'),
    path('delete/<review_id>', delete_review, name='delete_review'),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
]
