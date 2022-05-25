#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
python3 -m django startproject d06 .
python3 -m django startapp ex
python3 manage.py runserver