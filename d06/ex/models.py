from django.db import models

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tip(models.Model):
    contentue = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(auto_now=True)
    upvote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


class Vot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=0)


# # создание миграций (в папке migrations появится 0001_initial.py
# python3 manage.py makemigrations
#
# # посмотреть запрос для миграции (ex01 - название приложения, 0001 - номер миграции
# python3 manage.py sqlmigrate ex 0001
#
# # совершить миграцию в таблицу
# python3 manage.py migrate ex



#  python3 manage.py makemigrations
# python3 manage.py migrate
