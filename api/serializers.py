from rest_framework import serializers
from .models import File


class TextFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    data = serializers.CharField(max_length=10000)
    event_id = serializers.IntegerField()

