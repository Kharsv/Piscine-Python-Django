from django.shortcuts import render
from .models import Movies
from django.db import IntegrityError
# Create your views here.


def insert_data(request):
    result = list()
    try:
        mov1 = Movies(episode_nb=1,title='The Phantom Menace', director='George Lucas', producer="Rick McCallum",
                      release_date='1999-05-19')
        mov1.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('The Phantom Menace:')
        result.append(e)
    try:
        mov2 = Movies(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer="Rick McCallum",
                  release_date='2002-05-16')
        mov2.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('Attack of the Clones:')
        result.append(e)
    try:
        mov3 = Movies(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer="Rick McCallum",
                  release_date='2005-05-19')
        mov3.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('Revenge of the Sith:')
        result.append(e)
    try:
        mov4 = Movies(episode_nb=4, title='A New Hope', director='George Lucas', producer="Gary Kurtz, Rick McCallum",
                  release_date='1977-05-25')
        mov4.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('A New Hope:')
        result.append(e)
        print(e)
    try:
        mov5 = Movies(episode_nb=5, title='The Empire Strikes Back', director='George Lucas', producer="Gary Kutz, Rick McCallum",
                  release_date='1980-05-17')
        mov5.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('The Empire Strikes Back:')
        result.append(e)
    try:
        mov6 = Movies(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer="Howard G. Kazanjian, George Lucas, Rick McCallum",
                  release_date='1983-05-25')
        mov6.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('Return of the Jedi:')
        result.append(e)
    try:
        mov7 = Movies(episode_nb=7, title='The Force Awakens', director='J. J. Abrams', producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                  release_date='2015-12-11')
        mov7.save()
        result.append('Ok')
    except IntegrityError as e:
        result.append('The Force Awakens:')
        result.append(e)
    return render(request, 'ex03/insert_data.html', {'result':result})

def display(request):
    table = Movies.objects.all()
    return render(request, 'ex03/display.html', {"table":table})