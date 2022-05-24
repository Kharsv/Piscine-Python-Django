"""ex URL Configuration

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
from django.urls import path, include
# from ex00. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ex00.urls")),
    # path('', include views.home, name='home'),
    # path('login/', views.logins, name='login'),
    # path('registration/', views.registration, name='registration'),
    # path('logout/', views.logout_me, name='logout_me'),
    # path('like/', views.like_tip, name='like_tip'),
    # path('dislike/', views.dislike_tip, name='dislike_tip'),
    # path('delete/', views.delete, name='delete'),
    # path('upgrate/', views.upgrate, name='upgrate'),
]
