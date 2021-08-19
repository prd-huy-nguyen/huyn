from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetallCourseSerializer, CourseSerializer
# Create your views here.

class GetAllCouresAPIView(APIView):

    def get(self,request):
        list_course = Course.objects.all()
        myData = GetallCourseSerializer(list_course, many=True)
        return Response(data=myData.data, status=status.HTTP_200_OK)

    def post(self, request):
        myData = CourseSerializer(data=request.data)
        if not myData.is_valid():
            return Response('wrong valid', status=status.HTTP_400_BAD_REQUEST)
        title = myData.data['title']
        content = myData.data['content']
        price = myData.data['price']
        course = Course.objects.create(title=title, content=content, price=price)
        return Response(data=course.id, status=status.HTTP_201_CREATED)