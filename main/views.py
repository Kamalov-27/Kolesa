from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions





class One(APIView):
    def get(self):
        pass




class CarViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)


    def detail(self, request, id):
        car = Car.objects.get(id=id)
        serializer = CarSerializer(car, many=False)
        return Response(serializer.data)


    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def update(self, request, id):
        car = Car.objects.get(id=id)
        serializer = CarSerializer(instance=car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, id):
        car = Car.objects.get(id=id)
        car.delete()
        return Response("Deleted")



class CityViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


    # def detail(self, request, id):
    #     car = Car.objects.get(id=id)
    #     serializer = CarSerializer(car, many=False)
    #     return Response(serializer.data)


    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def update(self, request, id):
        city = City.objects.get(id=id)
        serializer = CarSerializer(instance=car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, id):
        city = City.objects.get(id=id)
        city.delete()
        return Response("Deleted")



class CategoryViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


    # def detail(self, request, id):
    #     car = Car.objects.get(id=id)
    #     serializer = CarSerializer(car, many=False)
    #     return Response(serializer.data)


    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def update(self, request, id):
        city = Category.objects.get(id=id)
        serializer = CategorySerializer(instance=car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, id):
        city = Category.objects.get(id=id)
        city.delete()
        return Response("Deleted")



class SubCategoryViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    def list(self, request):
        queryset = SubCategory.objects.all()
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)


    # def detail(self, request, id):
    #     car = Car.objects.get(id=id)
    #     serializer = CarSerializer(car, many=False)
    #     return Response(serializer.data)


    def create(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def update(self, request, id):
        city = SubCategory.objects.get(id=id)
        serializer = SubCategorySerializer(instance=car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, id):
        city = SubCategory.objects.get(id=id)
        city.delete()
        return Response("Deleted")
