from django.urls import path

from . import views


urlpatterns = [
    path('', views.hydroponic_system_list_create_view),
    path('<int:pk>/', views.hydroponic_system_detail_view, name='system-detail'),
    path('<int:pk>/sensor/', views.sensor_measurement_list_create_view)
]
