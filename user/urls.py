from django.urls import path, include
from . import views
from rest_framework import urls, routers

router = routers.DefaultRouter()
router.register(r'views', views.UserView, basename="user")

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
 ]