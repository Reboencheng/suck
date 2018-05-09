from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Grades,Students
def index(request):
    return HttpResponse('It`s ok')

def detail(request,num):
    return HttpResponse('datail-%s'%num)

def grade(requset):
    gradelist = Grades.objects.all()
    return  render(requset,'myApp/grades.html',{'grades':gradelist})

def student(requset):
    studentlist = Students.objects.all()
    return  render(requset,'myApp/students.html',{'students':studentlist})
def gradestudent(request,num):
    grade = Grades.objects.get(pk=num)
    studentlist = grade.students_set.all()
    return render(request,'myApp/students.html',{'students':studentlist})