from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, "base.html")


class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy('home')


class AuthenticationView(LoginView):
    form_class = LoginForm
    template_name = "authentication.html"

    def get_success_url(self):
        return reverse_lazy('profile')


def profile(request):
    return render(request, "profile.html")


def logout_user(request):
    logout(request)
    return redirect('home')
