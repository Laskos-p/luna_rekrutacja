from rest_framework.validators import UniqueTogetherValidator

from .models import HydroponicSystem

unique_system_name_for_user = UniqueTogetherValidator(
    queryset=HydroponicSystem.objects.all(),
    fields=['owner', 'name'],
    message='System already exists')
