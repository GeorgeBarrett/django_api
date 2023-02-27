from django.http import JsonResponse
from .models import Planet
from .serializers import PlanetSerializer

def planet_list(request):

    planets = Planet.objects.all()
    serializer = PlanetSerializer(planet_list, many=True)
    
    return JsonResponse(serializer.data, safe=False)
