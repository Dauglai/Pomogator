from rest_framework import viewsets, generics, permissions
from .models import Profile, Role
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer, RoleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAdminUser,)

class ProfileAPIList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProfileAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
