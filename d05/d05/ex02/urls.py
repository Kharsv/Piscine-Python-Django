from django.urls import path

from .views import create_sql
from .views import display
from .views import insert_data

urlpatterns = [
    path('init', create_sql),
    path('populate', insert_data),
    path('display', display),
]