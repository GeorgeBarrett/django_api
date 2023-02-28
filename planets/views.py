from django.http import JsonResponse
from .models import Planet
from .serializers import PlanetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def planet_list(request, format=None):

    if request.method == 'GET':
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
    
        return JsonResponse({"planets": serializer.data})
    
    if request.method == 'POST':
        serializer = PlanetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def planet_detail(request, id, format=None):

    try:
        planet = Planet.objects.get(pk=id)
    except Planet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlanetSerializer(planet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        planet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
