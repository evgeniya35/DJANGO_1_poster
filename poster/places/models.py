import re
from tabnanny import verbose
from django.db import models

from tinymce import models as tinymce_models

# Create your models here.


class Excursion(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description_short = models.TextField(
        verbose_name='Краткое описание',
        blank=True
    )
    description_long = tinymce_models.HTMLField(
        verbose_name='Полное описание',
        blank=True
    )
    lat = models.FloatField(
        verbose_name='Широта'
    )
    lon = models.FloatField(
        verbose_name='Долгота'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'


class Image(models.Model):
    excursion = models.ForeignKey(
        'Excursion',
        on_delete=models.CASCADE,
        verbose_name='Экскурсия',
        related_name='photos'

    )
    photo = models.ImageField(
        upload_to='photo',
        verbose_name='Файл изображения'
    )
    sort_index = models.PositiveSmallIntegerField(
        verbose_name='Порядок вывода',
        default=0
    )

    def __str__(self) -> str:
        return f'{self.sort_index} {self.excursion.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['sort_index']
