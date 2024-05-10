from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.hospital_list, name='map.urls'),
]