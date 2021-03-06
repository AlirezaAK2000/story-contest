from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import HttpResponse
from .models import Comment, Post
from django.views.generic import (
     ListView ,
      DetailView , 
      CreateView , 
      UpdateView ,
      DeleteView
)


def about(request):
    return render(request , 'about.html' , {'title': 'about'})

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    order = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title' , 'content' , 'image']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "comment_form.html"
    fields = ['content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    
    def post(self, request, postPk ,*args, **kwargs):
        self.post = Post.objects.get(pk=postPk)
        return super().post(request, *args, **kwargs)
        
            


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title' , 'content' , 'image']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
            



