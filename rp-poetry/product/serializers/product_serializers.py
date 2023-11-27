from rest_framework import serializers

from product.models.product import Category , Product
from product.serializers.category_seralizers import CategorySerializer

 class productserializer(serializers.ModelSerializer):
     Category = CategorySerializer(read_only=True, many=True)
     categories_id = serializers.PrimaryKeyRelatedField (queryset=Category.objects.all(), write_only=True, many=True)
    
    
 class Meta:
        model = Product
        fields = [
        'id',
        'title',
        'description',
        'price',
        'active',
        'category',
        'categories_id',
         ] 
        def create(self,validated_data):
            category_data = validated_data.pop('categories_id')
            
            Product = product.objects.create(**validated_data)
            for category in category_data:
                Product.category.add(category)
                
                return Product 