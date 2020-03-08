from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from .models import Country, Law
from django.shortcuts import get_object_or_404, redirect

authenticator = IAMAuthenticator('csrjtdcXxDn9g2a2sWsCs_2sdnoXag4ZofWBv54gKGYc')

assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/9e0b8c2d-9630-4f0b-a918-4c6469caeac7')
imb_access_token = 'Cmk8TYJ1tiMabs8usGqV'

def get_laws_in_country(country_id):
    country = get_object_or_404(Country, pk=country_id)
    laws  = Law.objects.filter(country=country)

    return laws
