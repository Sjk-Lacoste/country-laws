from django.contrib import admin
from .models import (
    Continent,
    Law,
    Country
)


# Register your models here.
admin.sites.register(Continent)
admin.sites.register(Law)
admin.sites.register(Country)