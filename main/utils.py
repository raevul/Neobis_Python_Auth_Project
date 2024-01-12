from django.core.mail import send_mail


def send_activation_code(user):
    subject = "django"
    message = f"hello {user.username}"
    from_email = "raevul@mail.ru"
    recipient_list = [user.email, ]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    print(f"Сообщение отправлено на {user.email}")


# subject = "Verify your email"
# message = f"""Thank you for registration in our site, please click on the link to verify your account: """
