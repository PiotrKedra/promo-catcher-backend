from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from app.models import Restaurant


def users(request):

    if request.method == 'GET':


        longitude = request.GET.get('longitude')
        latitude = request.GET.get('latitude')
        radius = request.GET.get('radius')

        # longitude = float(longitude)
        # latitude = float(latitude)
        # radius = float(radius)

        data = []

        for restaurant in Restaurant.objects.all():
            tmp = {
                'restaurant_name': restaurant.restaurant_name,
                'longitude': restaurant.longitude,
                'latitude': restaurant.latitude,
                'restaurant_url': restaurant.restaurant_url,
            }

            data.append(tmp)

        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'GET': None})
