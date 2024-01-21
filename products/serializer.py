
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """serializer for recipe."""

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'price', 'description','image','featured', 'active','address', 'room_count', 'bathroom_count' , 'square_meters']
        read_only_fields = ['id']
        
        
  