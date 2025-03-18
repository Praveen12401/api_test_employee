from django.urls import path
from .views import *

urlpatterns = [

    path("", index, name="Home"),

    path('employee_api/', employee_api, name='employee_api'),
]

