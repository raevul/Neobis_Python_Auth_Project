from django.core.mail import send_mail


def send_activation_code(user):
    send_mail(
        "Активация аккаунта",
        "Спасибо за регистрацию, теперь перейдите по ссылке чтобы подтвердить ваш аккаунт",
        "neobis@gmail.com",
        [user.email, ],
        fail_silently=False,
    )
