from django.contrib.auth.decorators import permission_required, user_passes_test
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from base.service import count_mail_all, count_active_mail, count_customer_all
from blog.models import Blog
from service.forms import CustomerForm, MessageForm, MailingForm
from service.models import Customers, Mailing, Message, TryMail
from service.sendmail import mail_customer


class HomePageView(TemplateView):
    template_name = 'service/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = Blog.objects.all().order_by('?')[:3]
        context_data['count_all_mail'] = count_mail_all()
        context_data['count_active_mail'] = count_active_mail()
        context_data['customer'] = count_customer_all()
        return context_data


def statistic(request):
    context = {
        'object_list': TryMail.objects.all()
    }
    return render(request, 'service/statistic.html', context)


class CustomerListView(ListView):
    model = Customers

    def get_queryset(self):
        return Customers.objects.filter(user_create=self.request.user)


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('service.view_mailing'):
            return queryset

        return queryset.filter(user_create=self.request.user)
class UserFilterMixin:
    def get_queryset(self):
        return self.model.objects.filter(user_create=self.request.user)

class MessageListView(ListView, UserFilterMixin):
    model = Message




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

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     form = context_data.get('form')
    #     return context_data


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


class CustomerUpdateView(UpdateView):
    model = Customers
    form_class = CustomerForm
    success_url = reverse_lazy('service:service')

    def get_queryset(self):
        return Customers.objects.filter(user_create=self.request.user)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('service:message')

    def get_queryset(self):
        return Message.objects.filter(user_create=self.request.user)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mail')

    def get_queryset(self):
        return Mailing.objects.filter(user_create=self.request.user)


class CustomerDeleteView(DeleteView):
    model = Customers
    success_url = reverse_lazy('service:service')

    def get_queryset(self):
        return Customers.objects.filter(user_create=self.request.user)


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('service:message')

    def get_queryset(self):
        return Message.objects.filter(user_create=self.request.user)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:mail')

    def get_queryset(self):
        return Mailing.objects.filter(user_create=self.request.user)


class CustomerDetailView(DetailView):
    model = Customers

    def get_queryset(self):
        return Customers.objects.filter(user_create=self.request.user)


class MailingDetailView(DetailView):
    model = Mailing

    def get_queryset(self):
        return Mailing.objects.filter(user_create=self.request.user)


class MessageDetailView(DetailView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(user_create=self.request.user)


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

