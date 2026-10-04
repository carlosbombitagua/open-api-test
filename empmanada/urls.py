"""empmanada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .decorators import docs_access_required

urlpatterns = [
    # La documentación de la API es solo para el grupo settings.DOCS_GROUP_NAME
    path('api/schema/', docs_access_required(SpectacularAPIView.as_view()), name='schema'),
    path('api/docs/', docs_access_required(SpectacularSwaggerView.as_view(url_name='schema')), name='swagger-ui'),
    path('api/redoc/', docs_access_required(SpectacularRedocView.as_view(url_name='schema')), name='redoc'),
    path('admin/', admin.site.urls),
    path('', include('manada.urls')),
    path('api/', include('rest_cliente.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
