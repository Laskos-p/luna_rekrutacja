from django.db import models


class HydroponicSystem(models.Model):
    name = models.CharField(max_length=100)