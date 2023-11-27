
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import  order_serializers

class Orderviewset(ModelViewSet):
    serializer_class = order_serializers
    queryset = Order.objects.all()
    