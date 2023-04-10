from msilib.schema import ListView

from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView

from service.forms import CustomerForm, MessageForm, MailingForm
from service.models import Customers, Message, Mailing


class UserFilterMixin:
    def get_queryset(self):
        return self.model.objects.filter(user_create=self.request.user)


class CustomerListView(ListView, UserFilterMixin):
    model = Customers


class MessageListView(ListView, UserFilterMixin):
    model = Message


class CustomerUpdateView(UpdateView, UserFilterMixin):
    model = Customers
    form_class = CustomerForm
    success_url = reverse_lazy('service:service')


class MessageUpdateView(UpdateView, UserFilterMixin):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('service:message')


class MailingUpdateView(UpdateView, UserFilterMixin):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mail')


class CustomerDeleteView(DeleteView, UserFilterMixin):
    model = Customers
    success_url = reverse_lazy('service:service')


class MessageDeleteView(DeleteView, UserFilterMixin):
    model = Message
    success_url = reverse_lazy('service:message')


class MailingDeleteView(DeleteView, UserFilterMixin):
    model = Mailing
    success_url = reverse_lazy('service:mail')


class CustomerDetailView(DetailView, UserFilterMixin):
    model = Customers


class MailingDetailView(DetailView, UserFilterMixin):
    model = Mailing


class MessageDetailView(DetailView, UserFilterMixin):
    model = Message
