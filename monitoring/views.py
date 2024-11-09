from django.shortcuts import render

from rest_framework import viewsets
from .models import Microservice, Deployment, ErrorRate
from .serializers import MicroserviceSerializer, DeploymentSerializer, ErrorRateSerializer

class MicroserviceViewSet(viewsets.ModelViewSet):
    queryset = Microservice.objects.all()
    serializer_class = MicroserviceSerializer

class DeploymentViewSet(viewsets.ModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer

class ErrorRateViewSet(viewsets.ModelViewSet):
    queryset = ErrorRate.objects.all()
    serializer_class = ErrorRateSerializer
