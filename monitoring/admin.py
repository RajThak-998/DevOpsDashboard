from django.contrib import admin
from .models import *


admin.site.register(Microservice)
admin.site.register(Deployment)
admin.site.register(ErrorRate)