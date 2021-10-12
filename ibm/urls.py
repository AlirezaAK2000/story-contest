from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^convert_post_to_speech/(?P<pk>\d{1,})/$' , views.convert_post_to_speech , name = 'convert_post_to_speech'),
    re_path(r'^convert_comment_to_speech/(?P<pk>\d{1,})/$' , views.convert_comment_to_speech , name = 'convert_comment_to_speech'),
    
]