from django.db import models
from django.contrib.auth.models import User

class order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.models.ForeignKey("user,on_delete=models.CASCADE ")
    
    