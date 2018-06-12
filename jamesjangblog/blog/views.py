from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list_view(request):
    posts = Post.blogposts.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail_view(request, year, month, day, post):
    posts = Post.published.all()
    tutpost = Post.tutorialposts.all()
    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html',  {'posts':posts, 'post' : post, 'tutpost' : tutpost})


def archived_post(request, post):
    post = get_object_or_404(Post, slug = post)
    return render(request, {'archive' : post})
    

