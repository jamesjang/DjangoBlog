from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm


def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, {'form': form}) 

def post_list_view(request):
    posts = Post.blogposts.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail_view(request, slug):
    posts = Post.published.all()
    tutpost = Post.tutorialposts.all()
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail_view', slug = slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post/detail.html', {'posts':posts, 'post' : post, 'tutpost' : tutpost, 'form': form})


def archived_post(request, post):
    post = get_object_or_404(Post, slug = post)
    return render(request, {'archive' : post})


    

