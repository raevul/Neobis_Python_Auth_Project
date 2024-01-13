from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("registration/", registration, name='register'),
    path("authentication/", AuthenticationView.as_view(), name='login'),
    path("verify_email/<str:uidb64>/<str:token>/", verify_email, name="verify_email"),
    path("logout/", logout_user, name='logout'),
    path("profile/", profile, name='profile'),
    path("password_reset/",
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name="password_reset"),
    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path("password_reset_confirm/<str:uidb64>/<str:token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password_reset_complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
    path("password_change/",
         auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name="password_change"),
    path("password_change_done/",
         auth_views.PasswordChangeView.as_view(template_name='password_change_done.html'),
         name="password_change_done"),
]
