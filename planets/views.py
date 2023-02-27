from django.http import JsonResponse
from .models import Planet
from .serialisers import PlanetSerialiser

def planet_list(request):

    planets = Planet.objects.all()
    serialiser = PlanetSerialiser(planet_list, many=True)
    
    return JsonResponse(serialiser.data)
