from django.contrib import admin
from .models import Product, ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "price", "count", "date", "description", "fullDescription", "free_delivery", "active",
    list_display_links = "pk", "title"
    ordering = "pk",
# Register your models here.

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "product", "image"
    list_display_links = "pk",
    ordering = "pk",


