from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf.urls import url, include
from markdownx import urls as markdownx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('writing/<slug:slug>', views.post_detail),
    path('projects/', views.projects),
    path("research/", views.research),
    path("uses/", views.uses),
    path("writing/", views.writing),
    path("downloads/", views.downloads),
    path("downloads/<slug:slug>", views.file),
    # path("designs/", views.designs),
]
urlpatterns += [
    url(r'^markdownx/', include('markdownx.urls'))
]
