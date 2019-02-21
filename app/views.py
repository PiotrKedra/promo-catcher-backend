from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

@login_required
def users(request):

    if request.method == 'GET':

        all_users = list(User.objects.values('id', 'username', 'email'))


        print(request.GET)
        return JsonResponse(all_users, safe=False)
    else:
        return JsonResponse({'GET': None})
