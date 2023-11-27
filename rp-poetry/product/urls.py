
from django.urls import path, include
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router = regiter(r'product', viewsets.productviewset,basename='product')

urlpatterns = [
 path('',include(router.urls)),   
]
