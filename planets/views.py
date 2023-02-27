from django.http import JsonResponse
from .models import Planet
from .serializers import PlanetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def planet_list(request):

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
def planet_detail(request):

    if request.method == 'GET':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass
