from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('map/', include('map.urls')),
    path("post/", include("post.urls")),
    path('mypage/', include('mypage.urls')), 
    path('api/accounts/v1/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
