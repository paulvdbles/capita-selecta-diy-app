from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import *


def home(request):
    from capitaselectadiy.models import Light
    all_light_objects = Light.objects.all()
    lights = {}

    # add all light information to object you can show in table
    for item in all_light_objects:
        lights[item.id] = {'name': item.name,
                           'ip': str(item.ip)}

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
            light = Light.objects.create(name=name, ip=ip)

            # add a message to the context
            context = {"type": "Light", "message": " added successfully!"}
            return render(request, "add_ light.html", context)
    else:
        return render(request, "add_ light.html")
