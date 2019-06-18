"""webhomework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import staticfiles
from django.urls import path

from django.conf.urls import include
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login_action/', views.login_action),
    path('event_manage/',views.event_manage),
    path('register/', views.register),
    path('add_user/', views.add_user),
    path('likemovie/', views.likemovie,name='likemovie'),
    path('unlikemovie/', views.unlikemovie,name='unlikemovie'),
    path('zengjia/', views.zengjia,name='zengjia'),
    path('jianshao/', views.jianshao,name='jianshao'),
    path('zengjiadianying/', views.zengjiadianying),
    path('jianshaodianying/', views.jianshaodianying)


]
urlpatterns+=staticfiles_urlpatterns()
