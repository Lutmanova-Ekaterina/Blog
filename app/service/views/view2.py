from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from service.models import TryMail, Mailing
from service.sendmail import mail_customer


def statistic(request):
    context = {
        'object_list': TryMail.objects.all()
    }
    return render(request, 'service/statistic.html', context)


def mail_customer_confirm(request):
    id = request.user.id
    mail_customer(id)
    return redirect(reverse('service:mail'))


@permission_required('service.turn_off')
def turn_off_mailing(request, pk):
    current_mailing = get_object_or_404(Mailing, pk=pk)
    if current_mailing:
        current_mailing.state_mail = Mailing.STATUSE_DEACTIVATION
        current_mailing.save()
    return redirect(request.META.get('HTTP_REFERER'))
