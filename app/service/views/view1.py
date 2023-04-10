from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from base.service import count_mail_all, count_active_mail, count_customer_all
from blog.models import Blog
from service.forms import CustomerForm, MailingForm, MessageForm
from service.models import Mailing, Customers, Message


class HomePageView(TemplateView):
    template_name = 'service/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = Blog.objects.all().order_by('?')[:3]
        context_data['count_all_mail'] = count_mail_all()
        context_data['count_active_mail'] = count_active_mail()
        context_data['customer'] = count_customer_all()
        return context_data


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('service.view_mailing'):
            return queryset

        return queryset.filter(user_create=self.request.user)


class CustomerCreateView(CreateView):
    model = Customers
    form_class = CustomerForm
    success_url = reverse_lazy('service:service')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user_create = self.request.user
            self.object.save()
        return super().form_valid(form)


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mail')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user_create = self.request.user
            self.object.save()
        return super().form_valid(form)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('service:message')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user_create = self.request.user
            self.object.save()
        return super().form_valid(form)
