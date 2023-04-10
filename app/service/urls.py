from django.urls import path

from service.apps import ServiceConfig
from service.views import *

app_name = ServiceConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customer/', CustomerListView.as_view(), name='service'),
    path('create_customer/', CustomerCreateView.as_view(), name='create_customers'),
    path('mail/', MailingListView.as_view(), name='mail'),
    path('message/', MessageListView.as_view(), name='message'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('create_mail/', MailingCreateView.as_view(), name='create_mail'),
    path('update_customer/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('update_message/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('update_mail/<int:pk>', MailingUpdateView.as_view(), name='update_mail'),
    path('delete_customer/<int:pk>', CustomerDeleteView.as_view(), name='delete_customer'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
    path('delete_mail/<int:pk>', MailingDeleteView.as_view(), name='delete_mail'),
    path('detail_customer/<int:pk>', CustomerDetailView.as_view(), name='detail_customer'),
    path('detail_mail/<int:pk>', MailingDetailView.as_view(), name='detail_mail'),
    path('detail_massage/<int:pk>', MessageDetailView.as_view(), name='detail_message'),
    path('mail_customer/', mail_customer_confirm, name='status'),
    path('statistic/', statistic, name='statistic'),
    path('deactivate_mail/<int:pk>', turn_off_mailing, name='deactivate'),

]
