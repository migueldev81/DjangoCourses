from django.urls import path
from apps.course.views import *
app_name = 'student'
urlpatterns = [
    path('courses', Course_APIView.as_view()),
    path('courses/<int:code>/', Course_APIView_Detail.as_view()),
    path('courses/name/<str:name>', Course_APIView_Querys.as_view())
]
