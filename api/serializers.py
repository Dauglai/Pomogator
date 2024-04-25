from rest_framework import serializers
from .models import GoogleDoc


class TextFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    data = serializers.CharField()

