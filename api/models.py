from django.contrib.auth.models import User
from django.db import models

from event.models import Event


class File(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    data = models.TextField()
    file_id = models.CharField(max_length=255, unique=True)
    folder_id = models.CharField(max_length=255)
    url = models.URLField(verbose_name="Ссылка")
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="мероприятие")

    def __str__(self):
        return self.name
