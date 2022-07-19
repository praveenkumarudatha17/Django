from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import AllCources,details,students
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import studentserializer

# Create your views here.
def Courses(request):
    ac=AllCources.objects.all()
    temp=loader.get_template("TechinalWeb/courses.html")
    context={"ac":ac}
    return HttpResponse(temp.render(context,request))
def detail(request,course_id):
    course=get_object_or_404(AllCources,pk=course_id)
    return render(request,'TechinalWeb/detail.html',{'course':course})

def yourchoice(request,course_id):
    course=get_object_or_404(AllCources,pk=course_id)
    try:
        selected_ct=course.details_set.get(pk=request.POST['choice'])
    except (KeyError,AllCources.DoesNotExists):
        return render(request,"TechinalWeb/detail.html",{
            'course':course,
            "error_message":"Select valid option"
        })
    else:
        selected_ct.choice=True
        selected_ct.save()
        return render(request,"TechinalWeb/detail.html",{'course':course})

class student_list(APIView):

    def get(self,request):
        students1=students.objects.all()
        serializer=studentserializer(students1,many=True)
        return Response(serializer.data)
    def post(self,hi):
        pass
def contact(request):
    return render(request,'TechinalWeb/detail.html',{'content':['contact','support@itsolutions.co']})