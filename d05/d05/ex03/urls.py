from django.urls import path

from .views import display
from .views import insert_data

urlpatterns = [
    path('populate', insert_data),
    path('display', display),
]