from rest_framework import serializers

from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='system-detail',
        lookup_field='pk'
    )

    class Meta:
        model = HydroponicSystem
        fields = [
            'url',
            'pk',
            'name'
        ]