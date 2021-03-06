import json
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

from .forms import *


def home(request):
    from capitaselectadiy.models import Light
    all_light_objects = Light.objects.all()
    lights = {}

    # add all light information to object you can show in table
    for item in all_light_objects:
        lights[item.ip] = {'name': item.name,
                           'ip': str(item.ip),
                           'state': item.state}

    context = {"lights": lights}
    return render(request, 'home.html', context)


@csrf_exempt
def addlight(request):
    if request.method == 'POST':  # add light to the database
        form = LightsForm(request.POST)
        if form.is_valid():
            # get input from the form
            name = form.cleaned_data['name']
            ip = form.cleaned_data['ip']

            # create light object
            from capitaselectadiy.models import Light
            light = Light.objects.create(name=name, ip=ip, state=False)

            # add a message to the context
            context = {"type": "Light", "message": " added successfully!"}
            return render(request, "add_ light.html", context)
    else:
        return render(request, "add_ light.html")


@csrf_exempt
def switch_light_on(request):
    # get the ip from the request and set a PUT request to the ip
    ip = request.POST.get('light_ip', None)
    requests.put('http://' + ip + '/ledon')

    # save the light on state to the database
    from capitaselectadiy.models import Light
    Light.objects.filter(pk=ip).update(state=True)

    return JsonResponse({'success': 'Light turned on'})


@csrf_exempt
def switch_light_off(request):
    # get the ip from the request and set a PUT request to the ip
    ip = request.POST.get('light_ip', None)
    requests.put('http://' + ip + '/ledoff')

    # save the light off state to the database
    from capitaselectadiy.models import Light
    Light.objects.filter(pk=ip).update(state=False)

    return JsonResponse({'success': 'Light turned off'})


@csrf_exempt
def delete_light(request):
    # get the ip from the request and set a PUT request to the ip
    ip = request.POST.get('light_ip', None)
    print(ip)

    # delete light from the database
    from capitaselectadiy.models import Light
    Light.objects.filter(pk=ip).delete()

    return JsonResponse({'success': 'Light is deleted'})
