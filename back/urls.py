from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('map/', include('map.urls')),
    path("post/", include("post.urls")),
    path('user/', include('user.urls')),
]