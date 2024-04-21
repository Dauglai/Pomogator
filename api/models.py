from django.db import models
from django.core.validators import RegexValidator


class TextFile(models.Model):
    name = models.CharField(
        max_length=56,
        verbose_name='Имя файла',
        help_text='Добавьте название вашего файла',
        unique=True,
        validators=[RegexValidator(regex=r'^[A-Za-zА-Яа-я0-9_]+\.txt$')]
    )
    data = models.TextField(
        verbose_name='Содержимое файла'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    link = models.CharField(max_length=1000,verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Текстовый файл'
        verbose_name_plural = 'Текстовые файлы'

    def __str__(self) -> str:
        return self.name