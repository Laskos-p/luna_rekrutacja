from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class HydroponicSystem(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class SensorMeasurement(models.Model):
    hydroponic_system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
