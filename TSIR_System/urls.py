"""TSIR_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login,name='login'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('upload/', views.upload,name='upload'),
    path('select/', views.select,name='select'),
    path('faqpage/', views.faqpage,name='faqpage'),
    path('extract/', views.extract,name='extract'),
    path('scan/', views.scan,name='scan'),
    path('user/', views.user,name='user'),
    path('collect/', views.collect, name='collect'),
    path('delete/', views.delete, name='delete'),
    path('delete1/', views.delete1, name='delete1'),
    path('lock/', views.lock, name='lock'),
    path('userEdit/', views.userEdit, name='userEdit'),
    path('calendar/', views.calendar, name='calendar'),
    path('recoverpw/', views.recoverpw, name='recoverpw'),
    path('pagesconfirmmail/', views.pagesconfirmmail, name='pagesconfirmmail'),
    path('chat/', views.chat, name='chat'),
    path('doctorlist/', views.doctorlist, name='doctorlist'),
    path('forum/', views.forum, name='forum'),
    path('neo4j/', views.neo4j, name='neo4j'),
    path("neo4j_extract_byGLM4/", views.neo4j_extract_byGLM4, name='neo4j_extract_byGLM4'),
    # path('neo4jView/', views.neo4jView, name='neo4jView'),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}, name='static'),

]