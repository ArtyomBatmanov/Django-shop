from django.urls import path
from .views import CategoriesList

urlpatterns = [
    # path('api/catalog/', Catalog.as_view(), name='products_list'),
    # path('api/banners/', BannersList.as_view(), name='banners'),
    path('categories/', CategoriesList.as_view(), name='categories'),
]

