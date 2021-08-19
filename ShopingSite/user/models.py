from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    phoneNumber = models.CharField(default='', max_length=15)
    address = models.CharField(default='',max_length=100)