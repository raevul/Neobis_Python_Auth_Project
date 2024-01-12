from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail


from .forms import RegisterForm, LoginForm
from .utils import send_activation_code


def home(request):
    return render(request, "home.html")


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_code(user)
            return render(request, "verification.html")
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "registration.html", context)


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
