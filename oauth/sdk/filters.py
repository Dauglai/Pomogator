import django_filters
from django.contrib.auth.models import User

from oauth.models import Profile


class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ("id", "email", "is_staff")