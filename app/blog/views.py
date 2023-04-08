from django.views.generic import ListView, DetailView
from blog.models import Blog


class ArticleListView(ListView):

    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('blog.set_publish'):
            return queryset

        return queryset


class ArticleDetailView(DetailView):

    model = Blog

