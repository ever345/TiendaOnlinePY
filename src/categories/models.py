from turtle import title
from django.db import models
from products.models import Products

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Products,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title