import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.

@csrf_exempt
def student_api(request):
    # for get data via third party app
    if request.method == 'GET' :
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, safe=False)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False )
    
    #  for data create via third party app
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res = 'Data Created'
            return JsonResponse(res, safe=False)
        else :
            return JsonResponse(serializer.errors, safe=False)
        
    # for update data via third party app
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        # serializer = StudentSerializer(stu, data=pythondata)
        #  for partial update, make partial=True
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            res = 'Data Updated'
            return JsonResponse(res, safe=False)
        else :
            return JsonResponse(serializer.errors, safe=False)
        
    # for delete data via third party app
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = 'Data Deleted'
        return JsonResponse(res, safe=False)
     
        