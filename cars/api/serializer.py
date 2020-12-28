from rest_framework import serializers
from cars.models import Cars


class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['id', 'car_brand', 'car_model',
                  'production_year', 'car_body', 'engine_type']

