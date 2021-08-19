from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexClass.as_view(), name="index" ),
    path('login/', views.LoginClass.as_view(), name="login"),
    path('userView/', views.ViewUser.as_view(), name='userView')
]