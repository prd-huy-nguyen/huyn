from django.urls import path
from .views import GetAllCouresAPIView

urlpatterns = [
    path('', GetAllCouresAPIView.as_view()),

]
