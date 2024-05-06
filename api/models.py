from django.db import models

from event.models import Event


class File(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    data = models.TextField()
    document_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="мероприятие")

    def __str__(self):
        return self.name