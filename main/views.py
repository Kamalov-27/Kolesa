import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


logger = logging.getLogger(__name__)



class One(APIView):
    def get(self):
        pass


@permission_classes([AllowAny])

class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        logger.info('car list')
        return Response(serializer.data)


    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('car created')

        return Response(serializer.data)
