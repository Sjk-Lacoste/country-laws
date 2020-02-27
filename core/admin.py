from django.contrib import admin
from .models import (
    Continent,
    Law,
    Country
)

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LawAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.sites.register(Continent, ContinentAdmin)
admin.sites.register(Law, LawAdmin)
admin.sites.register(Country, CountryAdmin)