from django.shortcuts import render
from .serializers import UserSerializer, UserViewSerializer
from .models import User
from rest_framework import generics, viewsets

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer