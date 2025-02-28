from django_filters import FilterSet, DateTimeFromToRangeFilter, RangeFilter

from .models import SensorMeasurement

class SensorMeasurementFilter(FilterSet):
    """
    Filters for range searching datetime and value of sensors
    """
    created_at = DateTimeFromToRangeFilter(field_name='created_at')
    value = RangeFilter(field_name='value')

    class Meta:
        model = SensorMeasurement
        fields = ['sensor_name', 'created_at', 'value']