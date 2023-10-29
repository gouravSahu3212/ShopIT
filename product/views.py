from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """
    A view class for handling HTTP GET and POST requests for the Product model.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 60 * 1))  # Cache the response for 1 hour
    def get(self, request, format=None):
        return self.list(request)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view class for retrieving, updating, and deleting a specific product.
    Inherits from the RetrieveUpdateDestroyAPIView class provided by the Django REST Framework.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
