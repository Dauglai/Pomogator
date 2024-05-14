from rest_framework import serializers
from .models import File


class CreateFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    data = serializers.CharField(max_length=10000)
    event_id = serializers.IntegerField()


class FileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    data = serializers.CharField()
    file_id = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    url = serializers.URLField()
    event_id = serializers.IntegerField()
