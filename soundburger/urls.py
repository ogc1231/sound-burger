"""soundburger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu.views import get_menu_list
from reviews.views import get_review_list, add_review, edit_review, delete_review
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('menu/', get_menu_list, name='get_menu_list'),
    path('reviews/', get_review_list, name='get_review_list'),
    path('add/', add_review, name='add_review'),
    path('edit/<review_id>', edit_review, name='edit_review'),
    path('delete/<review_id>', delete_review, name='delete_review'),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
]
