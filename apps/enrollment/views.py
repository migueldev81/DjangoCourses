from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.enrollment.serializers import EnrollmentSerializer

from apps.enrollment.models import Enrollment

from django.http import Http404


class Enrollment_APIView(APIView):
    def get(self, request):
        enrollment = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Enrollment_APIView_Details(APIView):
    def get(self,  request, id):
        enrollment = Enrollment.objects.get(pk=id)
        serilizer = EnrollmentSerializer(enrollment)
        return Response(serilizer.data)

    def put(self, request, id):
        enrollment = Enrollment.objects.get(pk=id)
        serializer = EnrollmentSerializer(
            enrollment, student=request.data.student, course=request.data.course)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        enrollment = Enrollment.objects.get(pk=id)
        enrollment.delete()
        return Response('Delete Enrollment')

        