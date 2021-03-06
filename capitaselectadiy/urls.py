"""capitaselectadiy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('add_light/', views.addlight, name='add_light'),
    url(r'^ajax/switch_light_on/$', views.switch_light_on, name='switch_light_on'),
    url(r'^ajax/switch_light_off/$', views.switch_light_off, name='switch_light_off'),
    path('ajax/delete_light/', views.delete_light, name='delete_light'),
    path('admin/', admin.site.urls),
]
