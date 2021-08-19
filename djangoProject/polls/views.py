from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from  django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomerForm, EmployeeForm
from .models import Question, Customer, TypeCustomer, Employee


# Create your views here.

class IndexClass(View):
    def get(self, request):
        listCustomer = Customer.objects.all()
        context = {"listCustomer": listCustomer}
        return render(request, "polls/index.html", context)

class viewListClass(View):
    def get(self,request):
        # lay tat ca du lieu cua Question
        listQuestion = Question.objects.all()
        context = {"listQuestion": listQuestion}
        return render(request, "polls/questionList.html", context)

class deleteCustomerClass(View):
    def get(self,request, customer_id):
        Customer.objects.get(pk=customer_id).delete()
        listCustomer = Customer.objects.all()
        context = {"listCustomer": listCustomer}
        return render(request, "polls/index.html", context)

def getObject(request):
    # lay tat ca du lieu cua Question
    listQuestion = get_object_or_404(Question, pk=1)
    context = {"listQuestion": listQuestion}
    return render(request, "polls/questionList.html", context)



class postClass(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = CustomerForm()
        return render(request, 'polls/create.html', {'form': form})

    def post(self, request):
        # kiem tra quyen cua user
        print(request.user.get_all_permissions())
        if request.method== 'POST':
            customer = CustomerForm(request.POST)
            # isvalid() hop le & hasperm la kioem tra xem thu no co quyen nay ko
            if customer.is_valid() and request.user.has_perm('polls.add_customer'):
                customer.save()
                return render(request, 'polls/create.html', {'check': "Đã lưu thành công"})
        return render(request, 'polls/create.html', {'form' : customer})

def viewEmployee(request):
    listEmployee = Employee.objects.all()
    return render(request, 'polls/employee.html',{'listEmployee': listEmployee})



# class postEmployee(LoginRequiredMixin,View):

def viewCreateEmployee(request):
    form = EmployeeForm()
    return render(request, 'polls/createEmployee.html', {'form': form})

def postEmployee(request):
    if request.method == 'POST':
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            employee.save(force_insert=True)
            return render(request, 'polls/employee.html', {'check': "Đã lưu thành công"})
    return render(request, 'polls/createEmployee.html', {'form': employee})