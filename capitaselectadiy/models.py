from django.db import models


class Light(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)