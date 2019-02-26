import sys

from django.http import JsonResponse

from app.models import Restaurant


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

        # TODO need to pick up closest restaurant, not all
        restaurants = Restaurant.objects.all()

        data = {}
        for restaurant in restaurants:
            tmp = {
                'longitude': restaurant.longitude,
                'latitude': restaurant.latitude,
                'restaurant_url': restaurant.restaurant_url,
            }
            data.update({restaurant.restaurant_name: tmp})

        return JsonResponse(data)
    else:
        return JsonResponse({'GET': None})
