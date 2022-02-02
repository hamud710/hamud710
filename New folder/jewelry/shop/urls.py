
from django.urls import path
from .import views

urlpatterns = [
    path('',views.shop,name = 'shop'),
    path('search',views.search,name = 'search'),
    path('details',views.details,name = 'details'),
    path('Cart',views.cart,name = 'cart'),
    path('<id>', views.Catshop, name='catshop'),
]