from django.contrib import admin
from .models import Variation, Category,Product
# Register your models here.

admin.site.register(Variation)
admin.site.register(Category)
admin.site.register(Product)