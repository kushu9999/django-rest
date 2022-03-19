from rest_framework import serializers
from .models import Student

# serializer class
class StudentSerializer(serializers.Serializer):  
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
  
# to create data in database via json  
    def create(self, validate_data):
      return Student.objects.create(**validate_data)