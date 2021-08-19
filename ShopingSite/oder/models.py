from django.db import models

# Create your models here.
from cart.models import Cart
from user.models import CustomerUser


class Oder(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shippingAddress = models.CharField(max_length=255,default='')
    orderDescription = models.TextField(default='')
    isCompleted = models.BooleanField(default=False)