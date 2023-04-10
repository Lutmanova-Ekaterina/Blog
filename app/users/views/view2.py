from datetime import datetime

import pytz
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from users.models import User
from users.service import generate_password_and_send_mail


def verify_email(request, token):
    current_user = User.objects.filter(token=token).first()
    if current_user:
        now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        if now > current_user.token_expired:
            current_user.delete()
            return render(request, 'users/verify_token_expired.html')

        current_user.is_active = True
        current_user.token = None
        current_user.token_expired = None
        current_user.save()
        return redirect('users:login')
    return render(request, 'users/verify_failed.html')


def simple_reset_password(request):
    if request.method == 'POST':
        current_user = User.objects.filter(email=request.POST.get('email')).first()
        if current_user:
            generate_password_and_send_mail(current_user)
        return render(request, 'users/simple_reset.html')


def confirm_new_generated_password(request):
    current_user = User.objects.filter(email=request.GET.get('email')).first()
    current_user.password = current_user.new_password
    current_user.new_password = None
    current_user.save()
    return redirect(...)


