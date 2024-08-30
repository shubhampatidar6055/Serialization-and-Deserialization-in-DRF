from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def student_detail(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data, content_type='application/json')

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res ={"msg":"Data created sucessfully"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse(JSONRenderer().render(serializer.errors),content_type='application/json')