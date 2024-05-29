from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import viewsets, generics, permissions

from .forms import ProfileForm
from .models import Profile, Role
from .serializers import ProfileSerializer, RoleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


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


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

def profile(request):
    error = ''
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        print(request.user.email)
        if profile_form.is_valid():
            try:
                Profile.objects.create(**profile_form.cleaned_data)
                return redirect('home')
            except:
                profile_form.add_error(None, "Ошибка добавления поста")
            return redirect('questions')
        else:
            error = 'Форма была неверной'

    profile_form = ProfileForm()
    enemies = Profile.objects.all()
    data = {
        'profile_form': profile_form,
        'error': error,
        'enemies': enemies
    }

    return render(request, 'profile.html', data)