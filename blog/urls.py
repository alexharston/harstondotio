from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path('^post/new/$', views.post_new, name='post_new'),
    re_path("^post/(?P<pk>\d+)/edit/$", views.post_edit, name='post_edit'),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("posts/", views.post_list, name="post_list"),
    path("research/", views.research, name="research"),
    path("designs/", views.designs, name="designs"),
    path("pay/", views.pay, name="pay"),
    path("cv/", views.cv, name="cv"),
]
