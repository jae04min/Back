from django.urls import path, include
from . import views
from rest_framework import routers
from .models import PostModel

router = routers.DefaultRouter()
router.register(r'content', views.PostViewSet, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    #path('view/', views.PostViewSet.as_view()),
    #path('view_create/', views.PersonViewSet),
]