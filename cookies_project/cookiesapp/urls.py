from django.urls import path
from django.shortcuts import redirect
from .views import add_to_cart, view_cart, clear_cart
def home(request):
    return redirect('view_cart')
urlpatterns = [
    path('',home,name='home'),
    path('addcart/', add_to_cart, name='add_to_cart'),
    path('viewcart/', view_cart, name='view_cart'),
    path('clearcart/', clear_cart, name='clear_cart'),
]
