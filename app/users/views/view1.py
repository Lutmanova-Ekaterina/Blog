from msilib.schema import ListView

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import SignupForm, SigninForm, CustomEditUserForm
from users.models import User
from users.service import set_verify_token_and_send_mail


class SigninView(LoginView):
    template_name = 'users/login.html'
    form_class = SigninForm


class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users:register_success')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            set_verify_token_and_send_mail(self.object)
            self.object.is_active = True
            self.object.save()
        return super().form_valid(form)


class SignupSuccessView(TemplateView):
    template_name = 'users/signup_success.html'


class VerifySuccessView(TemplateView):
    template_name = 'users/verify_success.html'


class UsersListView(ListView):
    model = User
    template_name = 'users/user_list.html'

@permission_required('users.change_status')
def user_status_change(request, pk):
    current_user = get_object_or_404(User, pk=pk)
    if current_user.is_superuser:
        return HttpResponseForbidden()
    if current_user.is_active:
        current_user.is_active = False
    else:
        current_user.is_active = True
    current_user.save()
    return redirect(request.META.get('HTTP_REFERER'))

class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/simple_reset.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('users:home')

    def get_object(self, queryset=None):
        return self.request.user
