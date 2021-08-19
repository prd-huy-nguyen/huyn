from django.db import models

# Create your models here.
from product.models import Variation
from user.models import CustomerUser


class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
