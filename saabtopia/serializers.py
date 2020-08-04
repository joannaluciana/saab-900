from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Producent, Car, Place, UserCar


class AdminProducentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producent
        fields = [
            'id',
            'name',
            'slug',
            'user',
            'image_url',
            'description',
            'url',
        ]

        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}


class ProducentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

class AdminCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'producent',
            'production',
            'car_class',
            'body_style',
            'engine',
            'transmission',
            'airconditioning',
            'length',
            'width',
            'height',
            'user',
            'description',
            'url',
        ]


class CarSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # pole przyjmie wartosc aktualnie zalogowanego usera


class AdminPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'user',
            'description',
            'url',
        ]


class PlaceSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminUserCarSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserCar
        fields = [
            'id',
            'name',
            'description',
            'place',
            'car',
            'date_come',
            'user',
            'image_url',
            'description',
        ]


class UserCarSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class UserSerializer():
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

