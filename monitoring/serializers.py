from rest_framework import serializers
from .models import Microservice, Deployment, ErrorRate

class MicroserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microservice
        fields = '__all__'

class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = '__all__'

class ErrorRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorRate
        fields = '__all__'