from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from places.admin import Excursion
from django.urls import reverse
from pprint import pprint


def show_index(request):
    places = Excursion.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lon, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places', args=[place.id])
                }
            }
        )
    excursions = {
        'type': 'FeatureCollection',
        'features': features
    }
    context = {'excursions': excursions}
    return render(request, 'index.html', context)


def places(request, place_id=1):
    place = get_object_or_404(Excursion, pk=place_id)
    place_context = {
        'title': place.title,
        'imgs': [img.photo.url for img in place.exc_photos.all().order_by('sort_index')],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lon
        }
    }
    return JsonResponse(place_context, json_dumps_params={'ensure_ascii': False})
