from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from api.mixins import UserQuerySetMixins

from .models import HydroponicSystem, SensorMeasurement
from .serializers import (
    HydroponicSystemSerializer,
    SensorMeasurementSerializer)


class HydroponicSystemListCreateAPIView(
    UserQuerySetMixins,
    generics.ListCreateAPIView
):
    """
    API endpoint for listing and creating hydroponic systems
    """

    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']

    @swagger_auto_schema(
        responses={200: HydroponicSystemSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        """
        Returns a list of all hydroponic systems owned by the logged user
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=HydroponicSystemSerializer,
        responses={201: HydroponicSystemSerializer},
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new hydroponic system for the logged user
        """
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        Save the hydroponic system with the logged user as the owner
        """
        serializer.save(user=self.request.user)


hydroponic_system_list_create_view = HydroponicSystemListCreateAPIView.as_view()


class HydroponicSystemDetailAPIView(
    UserQuerySetMixins,
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Returns detailed view for give hydroponic system
    """
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

    @swagger_auto_schema(
        responses={200: HydroponicSystemSerializer},
    )
    def get(self, request, *args, **kwargs):
        """
        Returns a list of all hydroponic systems owned by the logged user
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=HydroponicSystemSerializer,
        responses={200: HydroponicSystemSerializer},
    )
    def put(self, request, *args, **kwargs):
        """
        Fully update given hydroponic system
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=HydroponicSystemSerializer,
        responses={200: HydroponicSystemSerializer}
    )
    def patch(self, request, *args, **kwargs):
        """
        Partially update given hydroponic system
        """
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: "No Content"}
    )
    def delete(self, request, *args, **kwargs):
        """
        Delete given hydroponic system
        """
        return super().delete(request, *args, **kwargs)

hydroponic_system_detail_view = HydroponicSystemDetailAPIView.as_view()


class SensorMeasurementListCreateAPIView(
    generics.ListCreateAPIView
):
    """
    API endpoint for listing anc creating sensor data
    """
    queryset = SensorMeasurement.objects.all()
    serializer_class = SensorMeasurementSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'timestamp', 'value']
    ordering_fields = ['name', 'timestamp', 'value']

    @swagger_auto_schema(
        responses={200: SensorMeasurementSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        """
        Returns a list of all sensor measurements for given system
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=SensorMeasurementSerializer,
        responses={201: SensorMeasurementSerializer},
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new measurement for given system
        """
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        """
        Search for the system id in logged user systems
        """
        system_id = self.kwargs.get('pk')
        system = get_object_or_404(
            HydroponicSystem,
            pk=system_id,
            user=self.request.user
        )
        return SensorMeasurement.objects.filter(hydroponic_system=system)

    def perform_create(self, serializer):
        """
        Save the sensor measurement with the provided id as a system
        """
        system_id = self.kwargs.get('pk')
        system = get_object_or_404(
            HydroponicSystem,
            pk=system_id,
            user=self.request.user
        )
        serializer.save(hydroponic_system=system)


sensor_measurement_list_create_view = SensorMeasurementListCreateAPIView.as_view()
