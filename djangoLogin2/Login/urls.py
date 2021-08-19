from django.urls import path

from Login import views

urlpatterns = [
    path('', views.IndexClass.as_view(), name='index')
]
