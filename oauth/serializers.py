from rest_framework import serializers

from oauth.models import Profile, Role


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GoogleAuth(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
