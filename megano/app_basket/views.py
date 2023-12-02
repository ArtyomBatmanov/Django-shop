from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .basket import Basket
from .serializers import BasketSerializer
from app_products.models import Product


def get_products_in_basket(basket):
    products_in_basket = [product for product in basket.basket.keys()]
    products = Product.objects.filter(pk__in=products_in_basket)
    serializer = BasketSerializer(products, many=True, context=basket.basket)
    return serializer


class BasketOfProductsView(APIView):
    def get(self, *args, **kwargs):
        basket = Basket(self.request)
        serializer = get_products_in_basket(basket)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        basket = Basket(self.request)
        product = get_object_or_404(Product, id=self.request.data.get('id'))
        basket.add(product=product, count=self.request.data.get('count'))
        serializer = get_products_in_basket(basket)
        return Response(serializer.data)
    def delete(self, *args, **kwargs):
        print(self.request.data, '\n')
        basket = Basket(self.request)
        product = get_object_or_404(Product, id=self.request.data.get('id'))
        count = self.request.data.get('count', False)
        basket.remove(product, count=count)
        serializer = get_products_in_basket(basket)
        return Response(serializer.data)