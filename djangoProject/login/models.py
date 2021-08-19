from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    genderChoise = ((0, "Female"),(1,"Male"),(2,"Unknow"))
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=2, choices=genderChoise)
    address = models.CharField(max_length=255, default='')
    email = models.EmailField()