from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import *

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def addlight(request):
    if request.method == 'POST':
        form = LightsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            ip= form.cleaned_data['ip']

            from capitaselectadiy.models import Light
            light = Light.objects.create(
                name=name,
                ip=ip, )
    else:
        return render(request, "add_ light.html")