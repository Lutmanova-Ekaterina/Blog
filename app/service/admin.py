from django.contrib import admin

from service.models import Customers, Mailing, Message

admin.site.register(Customers)
admin.site.register(Mailing)
admin.site.register(Message)
