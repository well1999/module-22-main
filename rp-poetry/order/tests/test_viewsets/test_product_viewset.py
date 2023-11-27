import json 

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status 
from rest_framework.authtoken.models import Token

from django.urls import reverse 

from product.factories import CategoryFactory, ProductFactory
from order.factories import userfactory
from product.models import product

class TestProductViewset(APITestCase):
    client = APIClient 
    
    def setUp(self):
    self.user = UserFactory
    
    self.product = ProductFactory(
        title = 'pro controle',
        price = 200.00,
    )
    
    def test_get_all_product(self):
        response = self.client.get(
            reverse('product-list', kwargs={'versin': 'v1'})
        )
        
        self.assertEqual(response.status_code, statu.HTTP_200_OK)
        product_data = json.loads(response.content)
        
self.assertEqual(product_data[0]['title'], self.product.title)
self.assertEqual(product_data[0]['price'], self.product.Price)
self.assertEqual(product_data[0]['active'], self.product.Active)

def test_create_product(self):
    category = CategoryFactory
    data = json.dumps({
        'title': 'notebook',
        'price': 800.00,
        'categories_id': [category_id]
    } )
    
    response.self.client.post(
        reverse('product_list', kwargs = {'versin':'v1'}),
    data=data,
        content_type = 'aplication/json'
        
        
    
    )
 
 self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
 created_product = product.objects.get(title = 'notebook')
 
 self.assertEqual(created_product.title, 'notebook')
  self.assertEqual(created_product.price, '800.00'
                   )
 
 
    
    