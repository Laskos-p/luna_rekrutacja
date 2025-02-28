from rest_framework import serializers

from api.serializers import UserPublicSerializer

from .validators import unique_system_name_for_user
from .models import HydroponicSystem, SensorMeasurement


class HydroponicSystemSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(
        source='user',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='system-detail',
        lookup_field='pk'
    )

    class Meta:
        model = HydroponicSystem
        fields = [
            'owner',
            'url',
            'pk',
            'name',
            'created_at',
            'updated_at',
        ]
        validators = [
            unique_system_name_for_user
        ]


class SensorMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMeasurement
        fields = [
            'pk',
            'hydroponic_system',
            'sensor_name',
            'value',
            'created_at'
        ]
        read_only_fields = ['hydroponic_system']
