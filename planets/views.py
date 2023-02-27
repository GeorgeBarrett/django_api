from django.http import JsonResponse
from .models import Planet
from .serializers import PlanetSerializer

def planet_list(request):

    planets = Planet.objects.all()
    serializer = PlanetSerializer(planets, many=True)
    
    return JsonResponse({"planets": serializer.data})
