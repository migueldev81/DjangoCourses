from django.urls import path
from apps.enrollment.views import *
app_name = 'Enrollment'

urlpatterns = [
    path('v1/enrollment', Enrollment_APIView.as_view()),
    path('v1/enrollment/<int:id>/', Enrollment_APIView_Details.as_view()),
    # path('v1/enrollment/query', Enrollment_APIView_Querys.as_view()),

]
