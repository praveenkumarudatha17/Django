import json

from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from testapp.serializer import EmployeeSer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import io
# Create your views here.
# def EmployeeView(request):
#
@csrf_exempt
def Employeepost(request):
    if request.method == "POST" :
        json_data=request.body
       # print(json_data)
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        ser = EmployeeSer(data=pdata)
        if ser.is_valid():
            ser.save()
            res={"msg":"successfully created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(ser.errors)
        return HttpResponse(json_data,content_type='application/json')
    elif request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id != None:
            stu=Employee.objects.get(id=id)
            ser=EmployeeSer(stu)
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Employee.objects.all()
        ser = EmployeeSer(stu,many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == "PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id != None:
            emp=Employee.objects.get(id=id)
            ser=EmployeeSer(emp,data=pdata,partial=True)
            if ser.is_valid():
                ser.save()
                res={'msg':'Updated successfully'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(ser.errors)
            return HttpResponse(json_data,content_type='application/json')
        res={"msg": "ID is must be there"}
        json_data=JSONRenderer.render(res)
        return HttpResponse(json_data,content_type='application/json')
    else:
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id == None:
            res = {'msg':'Id must be required for deletion'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        emp=Employee.objects.get(id=id)
        emp.delete()
        res = {'msg': 'Resource deleted successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')