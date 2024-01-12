from django.urls import path, include

from .views import *

urlpatterns = [
    path("", home, name='home'),
    # path("registration/", RegistrationView.as_view(), name='register'),
    path("authentication/", AuthenticationView.as_view(), name='login'),
    # path("activate/<", ge, name=""),
    path("verification/", send_message, name='send_message'),
    path("logout/", logout_user, name='logout'),
    path("profile/", profile, name='profile'),
]
