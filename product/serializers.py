from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for converting Product model instances into JSON format.
    """
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'stock', 'image']

