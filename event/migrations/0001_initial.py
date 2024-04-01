# Generated by Django 5.0.3 on 2024-03-24 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Статус задания')),
            ],
        ),
        migrations.CreateModel(
            name='Type_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип ссылки')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('deadline', models.DateTimeField(verbose_name='Окончание мероприятия')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=10000, verbose_name='Описание')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event', verbose_name='Мероприятие')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.status', verbose_name='Готовность')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Ответсвенные')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('deadline', models.DateTimeField(verbose_name='Окончание Проекта')),
                ('events', models.ManyToManyField(to='event.event', verbose_name='Мероприятия')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tasks', models.ManyToManyField(to='event.task', verbose_name='Задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000, verbose_name='Название ссылки')),
                ('name', models.CharField(max_length=1000, verbose_name='Ссылка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event', verbose_name='Мероприятие')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.type_link', verbose_name='Тип ссылки')),
            ],
        ),
    ]