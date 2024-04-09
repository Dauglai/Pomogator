from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from .models import Role, AuthUser

admin.site.register(Role)
admin.site.register(AuthUser, UserAdmin)


