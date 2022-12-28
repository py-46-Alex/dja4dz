"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examp
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('school.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
