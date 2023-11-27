from django.db import models  
from product.models import category

class product(models.Model):
title = models.CharField(max_length=100)
description = models.TextField(max_length=500, blank=True, null=True)
price = models.PositiveIntegerField(null=True)
active = models.BooleanField(default=True)
category = models.ManyToManyField(category, blank=True)
