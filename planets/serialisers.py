from rest_framework import serializers
from .models import Planet

class PlanetSerialiser(serializers.ModelSerialiser):
    class Meta:
        model = Planet
        fields = ['id', 'name', 'desciption']