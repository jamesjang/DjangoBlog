from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list_view(request):
    return render(request, './blog/post/home.html')