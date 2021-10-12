from django.conf import settings
from ibm_watson import TextToSpeechV1 , NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(settings.IBM_TEXT_TO_SPEECH_API_KEY)

text_to_speech = TextToSpeechV1(authenticator=authenticator)

text_to_speech.set_service_url(settings.IBM_TEXT_TO_SPEECH_URL)


nlu_authenticator = IAMAuthenticator(settings.IBM_NLU_API_KEY)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=nlu_authenticator
)

natural_language_understanding.set_service_url(settings.IBM_NLU_URL)
