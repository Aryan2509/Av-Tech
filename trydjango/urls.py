"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more inform ation please see:
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
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from avtech import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about_view,  name='about' ),
    path('think/', views.think, name='think' ),
    path('think/ideas', views.think_ideas, name='think_ideas' ),
    path('innovate/', views.innovate_view, name='innovate' ),
    path('innovate/tunnel', views.tunnel_view, name='tunnel'),
    path('innovate/advisor', views.advisor_view, name='advisor'),
    path('upload/', views.upload,name='upload' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)