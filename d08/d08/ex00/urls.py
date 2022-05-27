
from django.contrib import admin
from django.urls import path
from ex00 import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]