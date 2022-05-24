
from django.db import models


# Create your models here.
class Movies(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    opening_crawl = models.TextField(blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
        return self.title


# # создание миграций (в папке migrations появится 0001_initial.py
# python manage.py makemigrations
#
# # посмотреть запрос для миграции (ex01 - название приложения, 0001 - номер миграции
# python manage.py sqlmigrate ex05 0001
#
# # совершить миграцию в таблицу
# python manage.py migrate ex05