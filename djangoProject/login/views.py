from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse("Xin chao, Tao da tro lai day ^^")

class LoginClass(View):

    def get(self, request):
        return render(request, 'login/login.html')

    def post(self,request):
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        # kiem tra username & password
        myUser = authenticate(username=userName, password=password)
        if myUser is None:
            return HttpResponse(" Dang nhap khong thanh cong")
        login(request,myUser)
        return render(request,'login/success.html')

#nen de Login truoc
class ViewUser(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
         return HttpResponse('<h3>View User </h3>')
    def post(self, request):
        pass
#cai nay dung cho ham
@decorators.login_required(login_url='/login/')
def viewCustomer(request):
    return HttpResponse('View Customer')