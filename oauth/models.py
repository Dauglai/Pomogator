from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from oauth.endpoint.services import get_path_upload_avatar, validate_size_image
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(models.Model):
    name = models.CharField(verbose_name='Роль', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class AuthUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
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
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    gmail = models.EmailField(verbose_name='Электронная почта Google', max_length=255, blank=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    @property
    def is_authenticated(self):
        return True


class SocialLink(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'