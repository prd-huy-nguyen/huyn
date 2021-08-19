from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
class TypeCustomer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(default=1,blank=False, null=False)
    address = models.CharField(max_length=200)
    gender = models.BooleanField()
    typeCustomer = models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(default=1, blank=False, null=False)
    address = models.CharField(max_length=200)
    gender = models.BooleanField()
    image =models.CharField(max_length=1000)

    def __str__(self):
        return self.name