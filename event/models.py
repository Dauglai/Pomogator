from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Event(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Окончание мероприятия')


    def __str__(self):
        return self.title




class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус задания')

    def __str__(self):
        return self.name


class Type_Link(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип ссылки')

    def __str__(self):
        return self.name


class Link(models.Model):
    link = models.CharField(max_length=10000, verbose_name='Название ссылки')
    name = models.CharField(max_length=1000, verbose_name='Ссылка')
    type = models.ForeignKey(Type_Link, on_delete=models.CASCADE, verbose_name='Тип ссылки')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=10000, verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Готовность')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Ответсвенные')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    def __str__(self):
        return self.title

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Окончание Проекта')
    events = models.ManyToManyField(Event, verbose_name='Мероприятия')
    tasks = models.ManyToManyField(Task, verbose_name='Задачи')

    def __str__(self):
        return self.title