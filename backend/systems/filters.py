from django_filters import FilterSet, DateTimeFromToRangeFilter

from .models import SensorMeasurement

class SensorMeasurementDateTimeFilter(FilterSet):
    """
    Filter the date and time range of sensor data
    """
    created_at = DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = SensorMeasurement
        fields = ['sensor_name', 'created_at', 'value']