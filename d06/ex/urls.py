from django.urls import path

from .views import home
from .views import logins
from .views import registration
from .views import logout_me
from .views import like_tip
from .views import dislike_tip
from .views import delete
from .views import upgrate


urlpatterns = [
    path('', home),
    path('login/', logins),
    path('registration/', registration),
    path('logout/', logout_me),
    path('like/', like_tip),
    path('dislike/', dislike_tip),
    path('delete/', delete),
    path('upgrate/', upgrate),
]