from service.models import Mailing, Customers


def count_mail_all(*args, **kwargs):
    """количество рассылок всего"""
    return Mailing.objects.all().count()


def count_active_mail(*args, **kwargs):
    return Mailing.objects.filter(state_mail='created').count()


def count_customer_all(*args, **kwargs):
    return Customers.objects.all().count()

