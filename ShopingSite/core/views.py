from django.shortcuts import render
from django.views import View
from product.models import Product, Category
# Create your views here.


class HomeView(View):
    def get(self,request):
        categorys =  Category.objects.all()
        context = {"categorys": categorys}
        return render(request,'homePage/index.html', context)