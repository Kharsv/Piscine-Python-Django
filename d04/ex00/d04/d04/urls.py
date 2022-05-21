"""d04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', include("ex00.urls")),
    # path('css/django', views.home, name='django'),
    # path('css/display', Home.as_view(), name='home'),
    path('ex01/', include("ex01.urls")),
    path('ex02/', include("ex02.urls")),
    # path('css/display', include("css.urls")),
    # path('css/templates/', include("css.urls")),

]
