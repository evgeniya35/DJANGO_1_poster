# Generated by Django 3.0 on 2022-02-21 10:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220216_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='lon',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='image',
            name='excursion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.Excursion', verbose_name='Экскурсия'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='', upload_to='photo', verbose_name='Файл изображения'),
            preserve_default=False,
        ),
    ]
