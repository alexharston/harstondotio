from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.post_list, name='post_list')

]