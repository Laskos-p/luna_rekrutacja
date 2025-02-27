from rest_framework import generics

from .models import HydroponicSystem
from .serializers import HydroponicSystemSerializer

class HydroponicSystemListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

hydroponic_system_list_create_view = HydroponicSystemListCreateAPIView.as_view()