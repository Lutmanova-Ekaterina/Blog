import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import request

from service.models import Mailing, TryMail


def mail_customer(id):
    mailing_item = Mailing.objects.filter(user_create=id)
    for item in mailing_item:
        if (
                item.state_mail == Mailing.STATUSE_CREATED or item.state_mail == Mailing.STATUSE_LAUNCHED) and item.first_date == datetime.date.today() and item.last_date >= datetime.date.today() and item.time_mailing >= datetime.datetime.now().time():
            item.state_mail = Mailing.STATUSE_LAUNCHED
            item.save()
            try:
                res = send_mail(
                    subject=item.add_message.topic_message,
                    message=item.add_message.letter,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[item.add_customer.email],
                    fail_silently=False,
                )

                if res:
                    item.state_mail = Mailing.STATUSE_COMPLETED
                    item.save()
                TryMail.objects.create(
                    status=item.state_mail,
                    answer=200,
                )
            except Exception as err:
                TryMail.objects.create(
                    status=item.state_mail,
                    answer=err,
                )
