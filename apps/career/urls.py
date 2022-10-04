from django.urls import path
from apps.career.views import *
app_name = 'career'

urlpatterns = [
    path('careers', Career_APIView.as_view()),
    path('careers/<str:code>/', Career_APIView_Detail.as_view()),
    path('careers/name/<str:name>', Career_APIView_Querys.as_view())
]
