from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("registration/", registration, name='register'),
    path("authentication/", AuthenticationView.as_view(), name='login'),
    # path("activate/<", ge, name=""),
    path("logout/", logout_user, name='logout'),
    path("profile/", profile, name='profile'),
]
