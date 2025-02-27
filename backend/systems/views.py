from platform import system

from asgiref.sync import sync_to_async
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from api.mixins import UserQuerySetMixins

from .models import HydroponicSystem, SensorMeasurement
from .serializers import HydroponicSystemSerializer, SensorMeasurementSerializer


class HydroponicSystemListCreateAPIView(
    UserQuerySetMixins,
    generics.ListCreateAPIView
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

hydroponic_system_list_create_view = HydroponicSystemListCreateAPIView.as_view()


class HydroponicSystemDetailAPIView(
    UserQuerySetMixins,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

hydroponic_system_detail_view = HydroponicSystemDetailAPIView.as_view()


class SensorMeasurementListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = SensorMeasurement.objects.all()
    serializer_class = SensorMeasurementSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'timestamp', 'value']
    ordering_fields = ['name', 'timestamp', 'value']

    def get_queryset(self):
        system_id = self.kwargs.get('pk')
        system = get_object_or_404(HydroponicSystem, pk=system_id, user=self.request.user)
        return SensorMeasurement.objects.filter(hydroponic_system=system)

    def perform_create(self, serializer):
        system_id = self.kwargs.get('pk')
        system = get_object_or_404(HydroponicSystem, pk=system_id, user=self.request.user)
        serializer.save(hydroponic_system=system)

sensor_measurement_list_create_view = SensorMeasurementListCreateAPIView.as_view()