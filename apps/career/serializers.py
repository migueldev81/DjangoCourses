from rest_framework import serializers
from apps.career.models import Career

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        exclude = []
