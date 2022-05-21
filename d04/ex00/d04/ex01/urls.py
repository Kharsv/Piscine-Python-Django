from django.urls import path

from .views import index
from .views import django
from .views import display
from .views import templates

urlpatterns = [
    path('', index),
    path('django', django),
    path('display', display),
    path('templates', templates),
]