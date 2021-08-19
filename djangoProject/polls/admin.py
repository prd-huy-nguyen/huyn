from django.contrib import admin
from .models import Question,Choice, TypeCustomer,Customer,Employee
# Register your models here.

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(TypeCustomer)
admin.site.register(Customer)
admin.site.register(Employee)