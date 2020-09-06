from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('post/<slug:slug   >', views.post_detail),
    path('projects/', views.projects),
    path("research/", views.research),
    path("design/", views.designs),
    path("uses/", views.uses),
    path("writing/", views.writing),
]
