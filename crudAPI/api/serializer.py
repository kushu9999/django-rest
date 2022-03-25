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
  
    def update(self, instance, validated_data):
        # before data validated
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        # after data validated
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        
        instance.save()
        return instance