from re import S
from django.shortcuts import render
from django.views import generic
from rest_framework.response import Response
from .serializers import EmployeesSerilizer
# from django.db import Employeemodel
# from django.views.generic import View
from rest_framework.views import APIView
from django.http import HttpResponse

# from loginpro.loginapp.models import EmployeeModel



# Create your views here.

class EmployeeAPIViews(APIView):
    def post(self,request):
            
            serializers=EmployeesSerilizer(request.data)
            if serializers.is_valid():
                eno=serializers.data.get('eno')
                return HttpResponse({'eno':eno,})
        #         esal=serializers.data.get('esal')
        #         ename=serializers.data.get('ename')
        #         eaddr=serializers.data.get('eaddr')
        #         return HttpResponse({'eno':eno,'esal':esal,'ename':eno,'eaddr':eaddr})




            
        
        
        
