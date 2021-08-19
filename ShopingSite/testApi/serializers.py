from rest_framework import serializers
from .models import Course

class GetallCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'price', 'content')

class CourseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=255)
    price = serializers.IntegerField(min_value=0)

    class Meta:
        model = Course
        fields = ('id', 'title', 'price', 'content')
