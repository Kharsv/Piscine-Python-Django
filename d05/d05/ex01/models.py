
from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    def __str__(self):
        return self.title

# # создание миграций (в папке migrations появится 0001_initial.py
# python3 manage.py makemigrations
#
# # посмотреть запрос для миграции (ex01 - название приложения, 0001 - номер миграции
# python3 manage.py sqlmigrate ex01 0001
#
# # совершить миграцию в таблицу
# python3 manage.py migrate ex01