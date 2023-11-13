from django.db import models
from app_catalog.models import Category


def product_image_directory_path(instanse: "ProductImage", filename):
    return f"products/images/{instanse.product.pk}/{filename}"


class Product(models.Model):
    title = models.CharField(max_length=128, blank=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, default=0, decimal_places=2, blank=False)
    count = models.IntegerField(default=0, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.CharField(max_length=256, blank=True)
    fullDescription = models.CharField(max_length=1028, blank=False)
    free_delivery = models.BooleanField(default=True, blank=False)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["pk", ]

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="product")
    image = models.FileField(upload_to=product_image_directory_path)

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"
        ordering = ["pk", ]

    def src(self):
        return self.image

    def __str__(self):
        return f"/{self.image}"

# {
#   "id": 123,
#   "category": 55,
#   "price": 500.67,
#   "count": 12,
#   "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
#   "title": "video card",
#   "description": "description of the product",
#   "fullDescription": "full description of the product",
#   "freeDelivery": true,
#   "images": [
#     {
#       "src": "/3.png",
#       "alt": "Image alt string"
#     }
#   ],
#   "tags": [
#     "string"
#   ],
#   "reviews": [
#     {
#       "author": "Annoying Orange",
#       "email": "no-reply@mail.ru",
#       "text": "rewrewrwerewrwerwerewrwerwer",
#       "rate": 4,
#       "date": "2023-05-05 12:12"
#     }
#   ],
#   "specifications": [
#     {
#       "name": "Size",
#       "value": "XL"
#     }
#   ],
#   "rating": 4.6
# }

# Create your models here.
