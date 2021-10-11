from django.conf.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView ,
    PostDetailView ,
    PostCreateView , 
    PostUpdateView ,
    PostDeleteView ,
    UserPostListView
    ) 

urlpatterns = [
    re_path(r'^$' , PostListView.as_view() , name = 'blog-home'),
    re_path(r'about/$' , views.about  ,name = 'blog-about') , 
    re_path(r'^post/(?P<pk>\d{1,})/$' , PostDetailView.as_view() , name='post-detail'),
    re_path(r'^post/new/$' , PostCreateView.as_view() , name='post-create'),
    re_path(r'^post/(?P<pk>\d{1,})/update/$' , PostUpdateView.as_view() , name='post-update'),
    re_path(r'^post/(?P<pk>\d{1,})/delete/$' , PostDeleteView.as_view() , name='post-delete'),
    re_path(r'^user/(?P<username>.*)/$' , UserPostListView.as_view() , name='user-posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)