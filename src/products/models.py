from distutils.command.upload import upload
from itertools import product
import uuid
from venv import create
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    slug = models.SlugField(null=False,blank=False,unique=True)
    image = models.ImageField(upload_to='madia/',null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)
    '''
    def __str__(self):
        return (self.title)
    
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
        while Products.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4()))[:8]
            )
    

pre_save.connect(set_slug, sender=Products)