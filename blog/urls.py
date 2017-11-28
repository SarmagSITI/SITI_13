from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #add new post
    url(r'^addpost/$', views.addpost, name='addpost'),
    #post list
    url(r'^postlist/$', views.postlist, name='postlist'),
    #post detail
    url(r'^postdetail/(?P<article_id>[0-9]+)$', views.postdetail, name='postdetail'),
]
