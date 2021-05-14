from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class One(APIView):
    def get(self):
        pass

@api_view(['GET', 'POST'])
def favorites_list(request):
    if request.method == 'GET':
        favorites = models.Favourites.objects.all()
        serializer = serializers.FavouritesSerializer(favorites, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.FavouritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def favorites_detail(request, favourite_id):
    try:
        favorite = models.Favourites.objects.get(id=favourite_id)
    except models.Favourites.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = serializers.FavouritesSerializer(favorite)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.FavouritesSerializer(instance=favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        favorite.delete()

        return Response({'deleted': True})

