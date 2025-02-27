from tkinter.ttk import Treeview

from rest_framework import serializers

from api.serializers import UserPublicSerializer

from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
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
            'name'
        ]