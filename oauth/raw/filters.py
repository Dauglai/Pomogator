import django_filters

from oauth.models import AuthUser


class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = AuthUser
        fields = ("id", "email", "is_admin")