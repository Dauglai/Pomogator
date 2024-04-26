from django.db import models
from django.core.validators import FileExtensionValidator
from oauth.services import get_path_upload_avatar, validate_size_image
import uuid
from django.contrib.auth.models import AbstractBaseUser, User


class Role(models.Model):
    name = models.CharField(verbose_name='Роль', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True, null=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.CASCADE, null=True, blank=True)
    group = models.CharField(verbose_name='Группа', max_length=10, null=True, blank=True)
    vk = models.CharField(verbose_name='ВКонтакте', max_length=10, null=True, blank=True)
    tg = models.CharField(verbose_name='Telegram', max_length=10, null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    gmail = models.EmailField(verbose_name='Электронная почта Google', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)
    USERNAME_FIELD = "gmail"

    def __str__(self):
        return self.gmail



class SocialLink(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'