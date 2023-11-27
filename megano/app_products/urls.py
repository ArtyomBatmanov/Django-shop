from django.urls import path
from .views import ProductDetail, CreateReview, TagsList, PopularList, LimitedList, SalesList

urlpatterns = [
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/reviews/', CreateReview.as_view()),
    path('tags/', TagsList.as_view(), name='tags_list'),
    path('products/popular/', PopularList.as_view(), name='popular'),
    path('products/limited/', LimitedList.as_view(), name='limited'),
    path('sales/', SalesList.as_view(), name='sales'),
]

