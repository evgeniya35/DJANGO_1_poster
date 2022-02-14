from tabnanny import verbose
from django.db import models

# Create your models here.

class Excursion(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description_short = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
        default=''
    )
    description_long = models.TextField(
        verbose_name='Полное описание',
        blank=True,
        default=''
    )
    lat = models.FloatField(
        verbose_name='Широта',
        default= 55
    )
    lon = models.FloatField(
        verbose_name='Долгота',
        default=37
    )

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'