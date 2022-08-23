from django.urls import path
from apps.course.views import *
app_name = 'student'
urlpatterns = [
    path('v1/course', Course_APIView.as_view()),
    path('v1/course/<int:code>/', Course_APIView_Detail.as_view()),
    path('v1/course/name/<str:name>', Course_APIView_Querys.as_view())
]
