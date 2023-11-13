from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CategorySerializer


class CategoriesList(APIView):
    def get(self, request: Request):
        categories = Category.objects.filter(parent=None)
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data)


