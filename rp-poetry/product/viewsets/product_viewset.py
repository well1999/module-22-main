from rest_framework.viewsets import ModelviewSet

from product.models import product 
from product.serializers.product_serializers import productserializer

class Productviewset(ModelViewSet):
    serializer_class = productserializer
 
def get_queryset(self):
        
       return product.objects.all.order_by("id")
  
   