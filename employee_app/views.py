from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Employee

def index(request):
    return render(request, "employee_app/employees.html")

def employee_api(request):
    employees = Employee.objects.all().values()
    return JsonResponse(list(employees), safe=False)

