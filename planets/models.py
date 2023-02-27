from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)