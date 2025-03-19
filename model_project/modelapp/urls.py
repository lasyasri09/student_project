from django.urls import path  
from . import views 
urlpatterns=[ 
    path('list/',views.student_list,name='student_list'),         
    path('add/',views.insert_student,name='insert_student'), 
] 