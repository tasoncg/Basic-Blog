from django.shortcuts import render
from .models import Author,Blog,Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.
class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5
    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')
    template_name='blog_list.html'


class BlogDetailView(generic.DetailView):
    model=Blog


class AuthorListView(generic.ListView):
    model = Author
    def get_queryset(self):
        return Author.objects.order_by('name')[:]
    template_name='author_list.html'
class AuthorDetailView(generic.DetailView):
    model = Author


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = Comment
    fields = ['content', ]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })








