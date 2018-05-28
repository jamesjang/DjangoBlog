from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list_view(request):
    posts = Post.tutorialposts.all()
    return render(request, './blog/post/tutorial.html', {'posts': posts})