from django.shortcuts import render
import psycopg2
from django.conf import settings


# Create your views here.
def create_sql(request):
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
        curr = conn.cursor()
        curr.execute("""CREATE TABLE IF NOT EXISTS ex02_movies (
        episode_nb serial PRIMARY KEY,
        title VARCHAR(64) UNIQUE NOT NULL,
        opening_crawl TEXT ,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
        );
        """
        )
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(e)
        result = e
    finally:
        if conn is not None:
            conn.close()
            result = 'Ok'

    return render(request, 'ex02/index.html', {'result': result})

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

    curr = conn.cursor()
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('The Phantom Menace:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES 
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum',  '2002-05-16')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('Attack of the Clones:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('Revenge of the Sith:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum',  '1977-05-25')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('A New Hope:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('The Empire Strikes Back:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
                VALUES
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')""")
        conn.commit()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('Return of the Jedi:')
        result.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
                VALUES
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11');""")
        conn.commit()
        conn.close()
        result.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        result.append('The Force Awakens:')
        result.append(e)
    return render(request, 'ex02/insert_data.html', {'result': result})

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
        curr.execute("""SELECT * FROM ex02_movies""")
        table = curr.fetchall()
        conn.close()
    except psycopg2.DatabaseError as e:
        table = 0
        print(e)
    return render(request, 'ex02/display.html', {'table':table})