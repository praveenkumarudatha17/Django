from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import EmployeeSer
from .models import Employee
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin



# Create your views here.
# class CL(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSer
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
# class RUD(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
# class CL(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSer
#
#
# class RUD(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSer

class CRUD(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]