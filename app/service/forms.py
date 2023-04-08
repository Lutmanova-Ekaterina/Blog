from django import forms

from base.forms import StyleFormMixin
from service.models import Customers, Mailing, Message


class CustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ['user_create', ]


class MailingForm(StyleFormMixin, forms.ModelForm):
    STATUSES = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
    )
    state_mail = forms.ChoiceField(choices=STATUSES, )

    class Meta:
        model = Mailing
        exclude = ['user_create', ]


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['user_create', ]
