from django.urls import path

from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.viewListClass.as_view(), name='viewList'),
    path('getObject/', views.getObject, name='getObject'),
    path('', views.IndexClass.as_view(), name='index'),
    path('index/', views.IndexClass.as_view(), name='index'),
    path('deleteCustomer/<int:customer_id>', views.deleteCustomerClass.as_view(), name='deleteCustomer'),
    path('create/', views.postClass.as_view(), name='save'),
    path('viewEmployee/', views.viewEmployee, name='viewEmployee'),
    path('createEmployee/', views.viewCreateEmployee, name='createEmployee'),
    path('postEmployee/', views.postEmployee, name='postEmployee'),
]
