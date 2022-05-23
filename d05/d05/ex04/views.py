from django.shortcuts import render
import psycopg2
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.
@csrf_exempt
def create_table(request):
    conn = 0
    try :
        # conn = psycopg2.connect(
        #     database = 'djangotraining',
        #     host='localhost',
        #     user='djangouser',
        #     password='secret',
        # )
        conn = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
    except:
        result = "I am unable to connect to the database."
        print(result)
    curr = conn.cursor()
    try:
        curr.execute("""CREATE TABLE IF NOT EXISTS ex04_movies (
        episode_nb serial PRIMARY KEY,
        title VARCHAR(64) UNIQUE NOT NULL,
        opening_crawl TEXT ,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
        );
        """)
        conn.commit()
        conn.close()
        result = 'Ok'
    except psycopg2.DatabaseError as e:
        print(e)
        result = e

    return render(request, 'ex04/index.html', {'result': result})

def insert_data(request):
    conn = 0
    result = list()
    try:
        # conn = psycopg2.connect(
        #     database = 'djangotraining',
        #     host='localhost',
        #     user='djangouser',
        #     password='secret',
        # )
        conn = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
    except:
        result = "I am unable to connect to the database."
        print(result)
    values = [[1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'],
              [2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'],
              [3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'],
              [4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'],
              [5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'],
              [6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum',
               '1983-05-25'],
              [7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11']]

    curr = conn.cursor()
    req = "INSERT INTO ex04_movies(episode_nb ,title, director, producer, release_date) VALUES (%d, '%s', '%s', '%s', '%s');"
    for x in values:
        try:
            curr.execute(req % (x[0], x[1], x[2], x[3], x[4]))
            conn.commit()
            result.append('Ok')
        except psycopg2.DatabaseError as e:
            print(e)
            conn.rollback()
            result.append(x[1])
            result.append(e)
        continue
    return render(request, 'ex04/insert_data.html', {'result': result})

def display(request):
    conn = 0
    result = list()
    try:
        # conn = psycopg2.connect(
        #     database = 'djangotraining',
        #     host='localhost',
        #     user='djangouser',
        #     password='secret',
        # )
        conn = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
    except:
        result = "I am unable to connect to the database."
        print(result)
    curr = conn.cursor()
    try:
        curr.execute("SELECT * FROM ex04_movies")
        table = curr.fetchall()
        conn.close()
    except psycopg2.DatabaseError as e:
        table = 0
        print(e)
    return render(request, 'ex04/display.html', {'table':table})


def delete(request):
    conn = 0
    try:
        # conn = psycopg2.connect(
        #     database = 'djangotraining',
        #     host='localhost',
        #     user='djangouser',
        #     password='secret',
        # )
        conn = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
    except:
        result = "I am unable to connect to the database."
        print(result)
    curr = conn.cursor()
    try:
            name = request.POST.get('name', "")
            query = "DELETE FROM ex04_movies WHERE title='%s';" % name
            curr.execute(query)
            rows_deleted = curr.rowcount
            conn.commit()
            conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    return rows_deleted


@csrf_exempt
def remove(request):
    conn = 0
    titles = None
    result = list()
    try:
        # conn = psycopg2.connect(
        #     database = 'djangotraining',
        #     host='localhost',
        #     user='djangouser',
        #     password='secret',
        # )
        conn = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
    except:
        result = "I am unable to connect to the database."
        print(result)
    curr = conn.cursor()
    try:
        rows = delete(request)
        curr.execute("SELECT title FROM ex04_movies;")
        titles = curr.fetchall()
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        titles = e
        print(e)
    return render(request, 'ex04/remove.html', {'titles': titles})
