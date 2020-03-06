from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Country,
    Law,
    Right
)

class CountryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class LawAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}

class RightAdmin(SummernoteModelAdmin):
    Summernote_fields = '__all__'
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Law, LawAdmin)
admin.site.register(Right, RightAdmin)