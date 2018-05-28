from django.conf.urls import url
from . import views
app_name = 'tutorials'

urlpatterns = [
  url(r'^$', views.post_list_view, name='post_list_view'),
]