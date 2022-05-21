#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
python3 -m django startproject d04
cd d04
python3 -m django startapp ex02
python manage.py runserver