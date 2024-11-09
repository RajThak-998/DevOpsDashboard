from django.db import models

class Microservice(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    status = models.CharField(max_length=20)
    last_checked = models.DateTimeField(auto_now=True)

class Deployment(models.Model):
    microservice = models.ForeignKey(Microservice, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    deployed_at = models.DateTimeField(auto_now_add=True)

class ErrorRate(models.Model):
    microservice = models.ForeignKey(Microservice, on_delete=models.CASCADE)
    rate = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)