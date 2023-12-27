from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("registration/", RegistrationView.as_view(), name='register'),
    path("authentication/", AuthenticationView.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("profile/", profile, name='profile'),
]
