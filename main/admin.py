from django.contrib import admin
from .models import Visit, Doctor, Service

admin.site.register(Visit)
admin.site.register(Doctor)
admin.site.register(Service)