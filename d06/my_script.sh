#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
python3 -m django startproject ex
cd ex
python3 -m django startapp ex00
python3 manage.py runserver