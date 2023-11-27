 from django.db import models    
 
 
 class product(models.Model):
     
     title = models.CharField(max_length=100) 
     description = models.TextField(max_length=500, blank=True, null=True)
     price = models.PositiveSmallIntegerField(null=True)
     active = models.BooleanField(default=True)
     categories = models.ManyToManyField(category,blank=True)
     