from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('post/<slug:id>', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new),
    path('post/<int:id>', views.post_edit),
    path('about/', views.about),
    path('projects/', views.projects),
    path('posts/', views.post_list),
    path("research/", views.research),
    path("designs/", views.designs),
    path("cv/", views.cv, name="cv"),
]
