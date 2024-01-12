from django.core.mail import send_mail


def send_activation_code(user):
    subject = "Verify your email"
    message = f"""Hello {user.username}, please click on the link to verify your account: """
    from_email = "pdjango73@gmail.com"
    recipient_list = [user.email, ]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    print(f"Сообщение отправлено на {user.email}")
