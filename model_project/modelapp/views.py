
from django.shortcuts import render, HttpResponse  
from .models import Student 
def insert_student(request): 
    student = Student(name="johndoe", age=22, email="john@example.com")
    student = Student(name="pushpa", age=19, email="pushpa@example.com")
    student = Student(name="swathi", age=19, email="swathi@example.com")
    student.save() 
    return HttpResponse("Student record added successfully!") 
def student_list(request): 
    students=Student.objects.all() 
    return render (request,'student_list.html',{'students':students}) 
# Create your views here.
