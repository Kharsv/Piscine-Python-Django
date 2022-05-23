from django.urls import path

from .views import create_sql

urlpatterns = [
    path('init/', create_sql),
]