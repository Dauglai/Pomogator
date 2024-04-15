from rest_framework import viewsets, generics, permissions
from .models import Event, Project
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, ProjectSerializer
from .models import Task, Type_Link, Status, Link
from .serializers import TaskSerializer, Type_LinkSerializer, StatusSerializer, LinkSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class EventAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EventAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class ProjectAPIList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProjectAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProjectAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class Type_LinkViewSet(viewsets.ModelViewSet):
    queryset = Type_Link.objects.all()
    serializer_class = Type_LinkSerializer



class StatusViewSet(viewsets.ModelViewSet):
    queryset = Type_Link.objects.all()
    serializer_class = StatusSerializer



class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LinkAPIList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LinkAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LinkAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
