from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    email_verify = models.BooleanField(default=False)
