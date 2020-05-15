"""entry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zymlover import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),
    path('gallery', views.gallery, name='gallery'),
    path('blog', views.blog, name='blog'),
    path('blog1', views.blog1, name='blog1'),
    path('contact', views.contact, name='contact'),
    path('index/book', views.book, name='book'),
    path('index/Login/', views.Login, name='Login'),
    path('index/signup', views.signup, name='signup'),
    path('comments', views.comments, name='comments'),
    path('index/search', views.search, name='search'),
]
