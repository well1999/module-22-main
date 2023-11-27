from rest_framework import  serializers

from product.models.category import Category

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 
                  'slug',
                  'description',
                  'active',
                  ]
        