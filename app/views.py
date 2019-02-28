import sys

from django.http import JsonResponse

from app.models import Restaurant
from implementation.common.distance import distance


def users(request):
    if request.method == 'GET':

        longitude = request.GET.get('longitude')
        latitude = request.GET.get('latitude')
        radius = request.GET.get('radius')

        if longitude is None or latitude is None or radius is None:
            return JsonResponse({
                'longitude': longitude,
                'latitude': latitude,
                'radius': radius
            })

        try:
            longitude = float(longitude)
            latitude = float(latitude)
            radius = float(radius)
        except TypeError as type_error:
            print(type_error)
            return JsonResponse({'Parsing went wrong': str(type_error)})
        except:
            print(sys.exc_info()[0])
            return JsonResponse({'Parsing went wrong': str(sys.exc_info()[0])})

        restaurants = Restaurant.objects.all()
        near_restaurants = []
        for restaurant in restaurants:
            if distance(latitude, longitude, restaurant.latitude, restaurant.longitude) <= radius:
                near_restaurants.append(restaurant)

        data = {}
        for restaurant in near_restaurants:
            tmp = {
                'longitude': restaurant.longitude,
                'latitude': restaurant.latitude,
                'restaurant_url': restaurant.restaurant_url,
            }
            data.update({restaurant.restaurant_name: tmp})

        return JsonResponse(data)
    else:
        return JsonResponse({'GET': None})
