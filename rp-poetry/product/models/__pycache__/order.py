from django.db import models as Model
from django.contrib.auth.models import User
 
from product.models import product

class order(models.Model):
    product = models.ManyToManyField(product, blank=False)
    user = models.models.ForeignKey(User, on_delete=models.CASCADE)