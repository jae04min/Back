from rest_framework import generics
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalListCreate(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer