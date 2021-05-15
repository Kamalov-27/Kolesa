from rest_framework import serializers

from diller import models


class FavouritesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    car_id = serializers.IntegerField()

    def create(self, validated_data):
        category = models.Favourites.objects.create(user=validated_data.get('user'),
                                                    car=validated_data.get('car'))
        return category

class ArchiveSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField()
    car = serializers.IntegerField()

    def create(self, validated_data):
        category = models.Favourites.objects.create(user=validated_data.get('user'),
                                                    car=validated_data.get('car'))
        return category

class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Publications
        fields = '__all__'