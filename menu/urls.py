from . import views
from django.urls import path


urlpatterns = [
    path('', views.BurgerList.as_view(), name='home')
]
