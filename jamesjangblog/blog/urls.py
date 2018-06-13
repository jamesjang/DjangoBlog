from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^$', views.archived_post, name='archived_post'),
    url(r'^(?P<slug>[-\w]+)/comment/', views.add_comment_to_post, name = 'add_comment_to_post')
]