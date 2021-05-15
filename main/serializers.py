from rest_framework import serializers
from .models import *






class CarSerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField('get_subcategory')
    class Meta:
        model = Car
        fields = ['name', 'description', 'subcategory']

    def get_subcategory(self, obj):
        subcategory = SubCategory.objects.filter(car_id=obj).values('name')
        return subcategory


class SubCategorySerializer(serializers.ModelSerializer):
    car_id = CarSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = '__all__'







class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
