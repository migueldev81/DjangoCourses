from rest_framework import serializers
from apps.enrollment.models import Enrollment
from apps.student.models import Student

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = ['date']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = []