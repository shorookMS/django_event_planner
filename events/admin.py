from django.contrib import admin
from .models import Event , BookedEvent

admin.site.register(Event)
admin.site.register(BookedEvent)