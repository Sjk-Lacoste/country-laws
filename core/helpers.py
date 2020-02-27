from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('csrjtdcXxDn9g2a2sWsCs_2sdnoXag4ZofWBv54gKGYc')

assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/9e0b8c2d-9630-4f0b-a918-4c6469caeac7')

