"""
URL configuration for feiralivre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.api.views import (EntregaViewSet, FrutaViewSet, ItemViewSet,
                           PagamentoViewSet, VerduraViewSet)
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Verdura', VerduraViewSet, basename='Verdura')
router.register(r'Fruta', FrutaViewSet, basename='Fruta')
router.register(r'entregas', EntregaViewSet, basename='entregas')
router.register(r'pagamentos', PagamentoViewSet, basename='pagamentos')
router.register(r'itens', ItemViewSet, basename='itens')


urlpatterns = [
    path("admin/", admin.site.urls),
]+router.urls
