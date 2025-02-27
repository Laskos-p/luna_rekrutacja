from rest_framework import serializers

from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.Serializer):
    class Meta:
        model = HydroponicSystem
        fields = [
            'name'
        ]