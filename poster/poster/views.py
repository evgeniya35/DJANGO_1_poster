from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from places.admin import Excursion
from django.urls import reverse
from pprint import pprint


def show_index(request):
    excurions = Excursion.objects.all()
    features = []
    for excurion in excurions:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [excurion.lon, excurion.lat]
                },
                'properties': {
                    'title': excurion.title,
                    'placeId': excurion.id,
                    'detailsUrl': reverse('places', args=[excurion.id])
                }
            }
        )
    attributes = {
        'type': 'FeatureCollection',
        'features': features
    }
    context = {'excursions': attributes}
    return render(request, 'index.html', context)


def places(request, place_id=1):
    excurion = get_object_or_404(Excursion, pk=place_id)
    place_context = {
        'title': excurion.title,
        'imgs': [img.photo.url for img in excurion.photos.all().order_by('sort_index')],
        'description_short': excurion.description_short,
        'description_long': excurion.description_long,
        'coordinates': {
            'lat': excurion.lat,
            'lng': excurion.lon
        }
    }
    return JsonResponse(place_context, json_dumps_params={'ensure_ascii': False})
