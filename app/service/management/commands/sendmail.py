from django.core.management import BaseCommand

from service.sendmail import mail_customer


class Command(BaseCommand):

    def handle(self, *args, **options):
        mail_customer()

