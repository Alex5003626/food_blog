from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Comment
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return self.object.post.get_absolute_url()
