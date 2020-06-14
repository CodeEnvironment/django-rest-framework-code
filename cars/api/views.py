
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CarsSerializer
from cars.models import Cars


class CarsAPIView(APIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request, *args, **kwargs):
        cars = self.get_queryset()
        serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data

        new_car = Cars.objects.create(car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarsSerializer(new_car)

        return Response(serializer.data)
