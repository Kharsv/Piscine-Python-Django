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
        curr.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
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