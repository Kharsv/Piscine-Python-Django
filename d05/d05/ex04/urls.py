from django.urls import path

from .views import create_table
from .views import display
from .views import insert_data
from .views import remove

urlpatterns = [
    path('init', create_table),
    path('populate', insert_data),
    path('display', display),
    path('remove/', remove),
]