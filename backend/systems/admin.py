from django.contrib import admin
from .models import HydroponicSystem, SensorMeasurement

@admin.register(HydroponicSystem)
class HydroponicSystemAdmin(admin.ModelAdmin):
    """
    Admin view for the HydroponicSystem model
    """
    list_display = ('id', 'name', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'user')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(SensorMeasurement)
class SensorMeasurementAdmin(admin.ModelAdmin):
    """
    Admin view for the SensorMeasurement model
    """
    list_display = ('id', 'hydroponic_system','sensor_name','value', 'created_at')
    list_filter = ('hydroponic_system', 'sensor_name', 'created_at')
    search_fields = ('hydroponic_system__name',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('hydroponic_system', 'sensor_name', 'value')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
