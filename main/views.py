from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from .forms import RegisterForm, LoginForm
from .utils import send_activation_token
from .token import account_activation_token


def home(request):
    return render(request, "home.html")


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_token(user, request)
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


def logout_user(request):
    logout(request)
    return redirect('home')


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        return redirect('regiter')

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "email_verified.html")


def profile(request):
    return render(request, "profile.html")


