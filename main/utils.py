from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

from .token import account_activation_token


def send_activation_token(user, request):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_url = request.build_absolute_uri(reverse('verify_email', args=[uid, token]))

    subject = "Verify email"
    message = f"""Hello {user.username}, please click on the link to verify your account: 
                  {verification_url}"""
    from_email = "pdjango73@gmail.com"
    recipient_list = [user.email, ]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
