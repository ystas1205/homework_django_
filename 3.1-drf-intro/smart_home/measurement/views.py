# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .models import Sensor, TemperatureMeasurement
# from .serializers import SensorSerialize



@api_view(['GET'])
def demo(request):
    # sensor = Sensor.objects.all()
    # ser = SensorSerializer(sensor, many=True)
    # print(sensor)
    data = {'message': 'hello'}

    return Response(data)
