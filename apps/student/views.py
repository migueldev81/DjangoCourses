from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.student.serializers import StudentSerializers

from apps.student.models import Student

from django.http import Http404


class Student_APIView(APIView):

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Student_APIView_Detail(APIView):

    def get_object(self, ci):
        try:
            return Student.objects.get(pk=ci)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, ci, format=None):
        student = Student.objects.get(pk=ci)
        serializer = StudentSerializers(student)
        res = serializer.data
        return Response(res)

    def put(self, request, ci, format=None):
        student = self.get_object(ci)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ci, format=None):
        student = self.get_object(ci)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Student_APIView_Querys(APIView):

    def get(self, request, name, format=None):
        student = Student.objects.get(name=name)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
