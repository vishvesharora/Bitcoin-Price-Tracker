from django.contrib import admin
from .models import Tracker

class TrackerAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Tracker,TrackerAdmin)