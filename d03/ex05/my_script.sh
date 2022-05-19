#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
django-admin startproject hello
cd hello
django-admin startapp helloworld
python manage.py runserver