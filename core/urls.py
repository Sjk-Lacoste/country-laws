from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('get_started/', get_started, name="get_started"),
    path('country-related-laws/<slug:slug>/', country_laws, name="country_related_laws")
]
