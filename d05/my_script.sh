#!/bin/sh

python -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
python3 -m django startproject d05
cd d05
python -m django startapp ex00
python -m django startapp ex01
python -m django startapp ex02
python -m django startapp ex03
python -m django startapp ex04
python manage.py runserver