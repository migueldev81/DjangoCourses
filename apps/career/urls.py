from django.urls import path
from apps.career.views import *
app_name = 'career'

urlpatterns = [
    path('v1/career', Career_APIView.as_view()),
    path('v1/career/<str:code>/', Career_APIView_Detail.as_view()),
    path('v1/career/name/<str:name>', Career_APIView_Querys.as_view())
]
