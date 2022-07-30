from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 9  # сколько мы будем выводить на страницу постов
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category') # <-- тот самый slug который в urls.py <slug:SLUG>


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"  # то, как будет называться объект, переданный в шаблон
    slug_url_kwarg = 'post_slug'


