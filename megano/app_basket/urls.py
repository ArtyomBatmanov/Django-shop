from django.urls import path

from .views import BasketOfProductsView


urlpatterns = [
    path('basket/', BasketOfProductsView.as_view(), name='basket'),
    path('cart/', BasketOfProductsView.as_view(), name='cart'),
]