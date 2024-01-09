from django.urls import path, include

from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("registration/", RegistrationView.as_view(), name='register'),
    path("authentication/", AuthenticationView.as_view(), name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", logout_user, name='logout'),
    path("profile/", profile, name='profile'),
]
