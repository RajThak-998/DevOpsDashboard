from celery import shared_task
from .models import Microservice
import requests

@shared_task
def check_microservice_health():
    microservices = Microservice.objects.all()
    for microservice in microservices:
        try:
            response = requests.get(microservice.url)
            microservice.status = 'Healthy' if response.status_code == 200 else 'Unhealthy'
        except requests.exceptions.RequestException:
            microservice.status = 'Unreachable'
        microservice.save()