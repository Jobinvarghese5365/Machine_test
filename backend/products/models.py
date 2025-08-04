from django.db import models

# Create your models here.
# products/models.py
from djongo import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.URLField()
