from django.urls import path

from .views import display
from .views import populate
from .views import remove

urlpatterns = [
    path('populate/', populate),
    path('display/', display),
    path('remove/', remove),
]