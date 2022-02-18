import requests

from django.db import transaction
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from urllib.parse import urlparse
from io import BytesIO

from places.models import Excursion, Image


class Command(BaseCommand):
    help = 'Загрузка данных из JSON'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='+',
            type=str,
            help='URL к файлу JSON'
        )


    def handle(self, *args, **options):
        self.stdout.write(f'Load data...{len(options["url"])}')
        for url in options["url"]:
            response = requests.get(url)
            response.raise_for_status()
            place_content = response.json()
            excursion, _created = Excursion.objects.update_or_create(
                title=place_content['title'],
                description_short=place_content['description_short'],
                description_long=place_content['description_long'],
                lat=place_content['coordinates']['lat'],
                lon=place_content['coordinates']['lng']
            )
            self.stdout.write(f'Load {excursion.title}')
            for num, img in enumerate(place_content['imgs'], start=1):
                response = requests.get(img)
                response.raise_for_status()
                image, _created = Image.objects.get_or_create(
                    sort_index=num,
                    excursion=excursion
                )
                image.photo.save(
                    urlparse(img).path.split('/')[-1],
                    BytesIO(response.content),
                    save=True
                )
                self.stdout.write(f'Load {image.photo.url}')