from django.db import models
from rest_framework import serializers

class EmployeesSerilizer(serializers.Serializer):
    eno=models.IntegerField()
    # ename=models.CharField(max_length=100)
    # esal=models.IntegerField()
    # eaddr=models.CharField(max_length=100)
