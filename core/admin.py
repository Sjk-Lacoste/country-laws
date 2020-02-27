from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Continent,
    Law,
    Country
)

class ContinentAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LawAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CountryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Law, LawAdmin)
admin.site.register(Country, CountryAdmin)