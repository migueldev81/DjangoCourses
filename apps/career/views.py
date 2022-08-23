from urllib import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.career.serializers import CareerSerializer
from apps.career.models import Career

from django.http import Http404

class Career_APIView(APIView):
    def get(self, request):
        career = Career.objects.all()
        serializer = CareerSerializer(career, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Career_APIView_Detail(APIView):
    def get_object(self, code):
        try:
            return Career.objects.get(pk=code)
        except Career.DoesNotExist:
            raise Http404

    def get(self, request, code):
        career = Career.objects.get(pk=code)
        serializer = CareerSerializer(career)
        res = serializer.data
        return Response(res)

    def put(self, request, code, format=None):
        career = self.get_object(code)
        serializer = CareerSerializer(career, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        career = Career.objects.get(pk=code)
        career.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Career_APIView_Querys(APIView):
    def get(self, request, name):
        career = Career.objects.get(name=name)
        serializer = CareerSerializer(career)
        return Response(serializer.data)
