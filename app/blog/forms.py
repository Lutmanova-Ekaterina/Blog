from django import forms

from blog.models import Blog


class BlogListForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['user_create']
