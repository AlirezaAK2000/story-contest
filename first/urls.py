
from django.contrib import admin
from django.urls import path
from django.conf.urls import re_path , include
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    
    re_path(r'', include('blog.urls')),
    
    re_path(r'' , include('users.urls')),
    
    re_path(r'^login/$' ,auth_views.LoginView.as_view(template_name = 'users/login.html') ,name = 'login' ),
    
    re_path(r'^logout/$' ,auth_views.LogoutView.as_view(template_name = 'users/logout.html') ,name = 'logout' ),
    
    re_path(r'^password-reset/$'
     ,auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html') ,
     name = 'password_reset' ),

    re_path(r'^password-reset-confirm/(?P<uidb64>.*)/(?P<token>.*)/$'
     ,auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html') ,
     name = 'password_reset_confirm' ),


    re_path(r'^password-reset/done/$'
     ,auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html') ,
     name = 'password_reset_done' ),

     re_path(r'^password-reset-complete/$'
     ,auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html') ,
     name = 'password_reset_complete' ),

]
