from django.contrib import admin
from .models import Event, Project, Task, Status

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Status)