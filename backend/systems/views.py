from platform import system

from asgiref.sync import sync_to_async
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import HydroponicSystem, SensorMeasurement
from .serializers import HydroponicSystemSerializer, SensorMeasurementSerializer


class HydroponicSystemListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)

hydroponic_system_list_create_view = HydroponicSystemListCreateAPIView.as_view()


class HydroponicSystemDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

hydroponic_system_detail_view = HydroponicSystemDetailAPIView.as_view()


class SensorMeasurementCreateAPIView(
    generics.CreateAPIView
):
    serializer_class = SensorMeasurementSerializer

    def perform_create(self, serializer):
        system_id = self.kwargs.get('pk')
        # print(system_id)
        system = get_object_or_404(HydroponicSystem, pk=system_id, user=self.request.user)
        print(system)
        serializer.save(hydroponic_system=system)

sensor_measurement_create_view = SensorMeasurementCreateAPIView.as_view()