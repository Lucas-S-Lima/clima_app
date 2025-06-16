from django.contrib import admin
from .models import City, Alert, Temperature


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city',]
    search_fields = ['city']


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['city', 'operator', 'temperature', 'message', 'created_at', 'active'] 
    search_fields = ['city', 'operator', 'temperature']


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'city', 'created_at']
    search_fields = ['temperature', 'city']