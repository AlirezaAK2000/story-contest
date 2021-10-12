from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^convert_text_to_speech/(?P<pk>\d{1,})/$' , views.convert_text_to_speech , name = 'convert_text_to_speech'),
]