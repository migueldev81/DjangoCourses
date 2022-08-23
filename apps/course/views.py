from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.course.serializers import CourseSerializer
from apps.course.models import Course
from django.http import Http404


class Course_APIView(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Course_APIView_Detail(APIView):

    def get_object(self, code):
        try:
            return Course.objects.get(pk=code)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        course = Course.objects.get(pk=code)
        serializer = CourseSerializer(course)
        res = serializer.data
        return Response(res)

    def put(self, request, code, format=None):
        course = Course.objects.get(pk=code)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        course = self.get_object(code)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Course_APIView_Querys(APIView):
    def get(self, request, name, format=None):
        course = Course.objects.get(name=name)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
