from django.db import models

# Create your models here.
class data(models.Model):
    Brand= models.CharField(max_length=100)
    Product= models.CharField(max_length=100)
    cost=models.CharField(max_length=100)