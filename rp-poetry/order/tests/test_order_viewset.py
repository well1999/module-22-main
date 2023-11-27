impor JSON

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.urls import reverse



from product.factories import CategoryFactory, ProductFactory
from order.factories import userfactory, OrderFactory
from product.models import product
from order.models import order 

class testorderviewset(APITestCase):
    
    client = APIClient
    
    def setUp(self):
 self.user = UserFactory()
 Token = Token.objects.create(user=self.user) 
 Token.save() #added 
 
 self.product = ProductFactory(
     title = 'pro controller',
 )
 
 def test_order(self):
     response = self.client.get(
         reverse('order_list', kwargs={'version': 'v1'})
     ) 
  self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  
 order_data = json.loads(response.content)[0]
 self.assertEqual(order_data['product'][0]['title'], self.product.title)
 self.assertEqual(order_data['product'][0]['price'], self.product.price)
 self.assertEqual(order_data['product'][0]['active'], self.product.active) 
 self.assertEqual(order_data['product'][0]['category'][0]['title'], self.category.title)
 
 def test_create_order(self):
     user = userfactory()
     product = ProductFactory()
     data = json.dumps({
         'product_id': [product.id],
         'user': user.id
     }) 
 
 response = self.client.post(
     reverse('order-list', kwargs={'version':1}),
     data = data,
     content_type = 'aplication/json'
 )
 
 self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 created_order = Order.objects.get(user=user)
 
 
 
      
