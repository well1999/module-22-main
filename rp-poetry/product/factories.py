import factory
from product.models import product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
 title = factory.faker('pystr')
 slug = factory.faker('pystr')
 description = factory.faker('pystr')
  title = factory.iterator([true, False]) 
  
  class Meta:
      model = Category
      
 class CategoryFactory(factory.django.DjangoModelFactory):
   price = factory.faker('pystr')
 Category = factory.LazyAttribute('categoryfactory')
  title = factory.faker('pystr')
  
  @factory.post_generation
  def category(self,create,extracted, **kwargs):
      if not create:
          return
      if extracted:
          for category in extracted:
              self.category.add(Category) 
              
              
class Meta:
    model = product
      