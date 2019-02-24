from django.contrib import admin
from .models import Host, Nanny, Schedule
# Register your models here.
admin.site.register(Host)
admin.site.register(Nanny)
admin.site.register(Schedule)
