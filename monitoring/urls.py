from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .views import MicroserviceViewSet, DeploymentViewSet, ErrorRateViewSet

router = DefaultRouter()
router.register(r'microservices', MicroserviceViewSet)
router.register(r'deployments', DeploymentViewSet)
router.register(r'errorrates', ErrorRateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', lambda request: redirect('api/', permanent=True)),  # Redirect to '/api/'
]