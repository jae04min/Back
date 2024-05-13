from django.urls import path
from . import views

urlpatterns = [
    path('hospitals/', views.HospitalListCreate.as_view(), name='hospital-list-create'),
    path('hospitals/<int:pk>/', views.HospitalRetrieveUpdateDestroy.as_view(), name='hospital-retrieve-update-destroy'),
]