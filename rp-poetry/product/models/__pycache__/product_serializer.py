from rest_framework import serializers
from product.models.product import Product

from product.serializers.category_seralizers import CategorySerializer

class ProducrSerializer(serializers.ModelSerializer):
    category =CategorySerializer(required=True, many=True)
class meta:
    model = Product
    fields = [
        'title'
        'description'
        'price'
        'active'
        'category',
    ]