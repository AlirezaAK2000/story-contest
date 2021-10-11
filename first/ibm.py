from django.conf import settings
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(settings.IBM_TEXT_TO_SPEECH_API_KEY)

text_to_speech = TextToSpeechV1(authenticator=authenticator)

text_to_speech.set_service_url(settings.IBM_TEXT_TO_SPEECH_URL)

