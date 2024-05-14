from rest_framework import serializers
from api.serializers import FileSerializer
from .models import Event, Project
from rest_framework import serializers
from .models import Task, Status


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



class EventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tasks = TaskSerializer(source="task_set", many=True, read_only=False)
    files = FileSerializer(source="file_set", many=True, read_only=False)
    class Meta:
        model = Event
        fields = '__all__'
        depth = 2


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = '__all__'
        depth = 2


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'