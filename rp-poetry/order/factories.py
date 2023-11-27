import Factory
from django.contrib.auth.models import User
from product.factories import ProductFactory

from order.models import Order

class userfactory(Factory.django.DjangoModelFactory):
   email = Factory.Faker('pystr') 
   username = Factory.Faker('pystr')
   
   class Meta:
       model = User
       
       class orderfactory(Factory.django.DjangoModel):
           User = Factory.SubFactory(userfactory)
           
@Factory.post_generation
def product(self, create,extracted,**kwargs):
    if not create:
        return
    
    if extracted:
        for product in extracted:
            self.product.add(product) 
            
            class meta:
                model = Order
        