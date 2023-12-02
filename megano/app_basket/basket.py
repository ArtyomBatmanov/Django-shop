from decimal import Decimal
from megano import settings
from app_products.models import Product


class Basket(object):
    """
    Класс корзина
    """

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, count):
        """
        Добавление продукта в корзину, обновление его количества.
        """
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'count': count,
                                     'price': str(product.price)}
        else:
            self.basket[product_id]['count'] += count
        self.save()

    def save(self):
        """
        Сохранение корзины
        """
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def remove(self, product, count):
        """
        Удаление продукта из корзины или уменьшение количества продукта.
        """
        product_id = str(product.id)
        if product_id in self.basket:
            if count == 1 and self.basket[product_id]['count'] > 1:
                self.basket[product_id]['count'] -= int(count)
            else:
                del self.basket[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['count']
            yield item

    def total_count(self):
        """
        Подсчет всех продуктов в корзине.
        """
        return sum(item['count'] for item in self.basket.values())

    def total_price(self):
        """
        Подсчет стоимости продуктов в корзине.
        """
        return sum(Decimal(item['price']) * item['count'] for item in
                   self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True