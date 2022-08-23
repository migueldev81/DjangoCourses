from django.urls import path
from apps.student.views import *
app_name = 'student'
urlpatterns = [
    path('v1/student', Student_APIView.as_view()), 
    path('v1/student/<int:ci>/', Student_APIView_Detail.as_view()),
    path('v1/student/name/<str:name>/', Student_APIView_Querys.as_view()),

]