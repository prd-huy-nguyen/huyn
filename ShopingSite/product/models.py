from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='', max_length=200)
    slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(default='', max_length=200)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.title

class Variation(models.Model):
    title = models.CharField(default='', max_length=200)
    product=  models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    salePrice = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title