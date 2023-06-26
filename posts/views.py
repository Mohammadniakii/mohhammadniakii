from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views import generic

from .models import Post, Comment
from .forms import PostForm



def index(request) :
    #body
    return HttpResponse('<h1>welcome to django</h1>')


def home(request):
    return HttpResponse('<h1>weclome to my blog dude</h3>')


def Post_List(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context=context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


def post_detail(request, post_id):
    #try:
     #       post = Post.objects.get(pk=post_id)
    #post = Post.DoesNotExist:
    #       return HttpResponseNotFound('post is not exist!')
    post = get_object_or_404(Post, pk=post_id )
    comments = Comment.objects.filter(post=post)
    context = {'post':post, 'comments':comments}
    return render(request, 'posts/post_detail.html', context=context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #print(type(form.cleaned_data))
            #print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()

    return render(request, '/posts/post_create.html', {'form': form})
