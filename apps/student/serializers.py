from rest_framework import serializers
from apps.student.models import Student
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student  
        exclude = []