"""django_website2 URL Configuration

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
from django.urls import path, include
from website import views as web
from text_edit import views as text
from scraping import views as scr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web.IndexView.as_view()),
    path('about/', web.AboutView.as_view()),
    path('text_edit/', text.Index.as_view()),
    #path('scraping/', scr.Index.as_view()),
    path('scraping/', include('scraping.urls')), 
]
