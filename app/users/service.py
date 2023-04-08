from datetime import datetime, timedelta
from django.conf import settings

import pytz
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.urls import reverse
from users.models import User


def set_verify_token_and_send_mail(new_user):
    now = datetime.now(pytz.timezone(settings.TIME_ZONE))
    new_user.is_active = False
    new_user.token = User.objects.make_random_password(length=20)
    new_user.token_expired = now + timedelta(hours=72)
    new_user.save()

    link_to_verify = reverse('users:verify_email', args=[new_user.token])
    send_mail(
        subject='Подтвердите почту',
        message=f'{settings.BASE_URL}{link_to_verify}',
        recipient_list=[new_user.email],
        from_email=settings.EMAIL_HOST_USER
    )


def generate_password_and_send_mail(user):
    new_password = User.objects.make_random_password(length=20)
    user.new_password = make_password(new_password)
    user.save()
    send_mail(
        subject='Новый пароль',
        message=f'{new_password}',
        recipient_list=[user.email],
        from_email=settings.EMAIL_HOST_USER
    )
