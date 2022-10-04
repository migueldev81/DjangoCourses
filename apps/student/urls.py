from django.urls import path
from apps.student.views import *
app_name = 'student'
urlpatterns = [
    path('students', Student_APIView.as_view()), 
    path('students/<int:ci>/', Student_APIView_Detail.as_view()),
    path('students/name/<str:name>/', Student_APIView_Querys.as_view()),

]