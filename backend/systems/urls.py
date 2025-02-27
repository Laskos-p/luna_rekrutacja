from django.urls import path

from . import views


urlpatterns = [
    path('', views.hydroponic_system_list_create_view)
]