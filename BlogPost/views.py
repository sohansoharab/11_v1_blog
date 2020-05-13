from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from BlogPost.models import Post

# Create your views here.


def about(request):
    return render(request, 'BlogPost/about.html')


class PostList(ListView):
    model = Post
    template_name = 'BlogPost/index.html'
    context_object_name = 'all_post'


class PostDetails(DetailView):
    model = Post
    template_name = 'BlogPost/postdetail.html'
    context_object_name = 'current_post'


class CreatePost(CreateView):
    model = Post
    template_name = 'BlogPost/post_new.html'
    fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'BlogPost/update_post.html'
    fields = [
        'title',
        'description'
    ]


class DeletePost(DeleteView):
    model = Post
    template_name = 'BlogPost/delete_post.html'
    success_url = reverse_lazy('home')

