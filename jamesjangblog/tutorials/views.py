from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def post_list_view(request):
    posts = Post.tutorialposts.all()
    tutpost = Post.tutorialposts.all()
    return render(request, './blog/post/tutorial.html', {'posts': posts, 'tutpost' : tutpost})


