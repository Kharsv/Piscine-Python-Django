#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
#python3 -m django startproject d07
cd d07
#python3 -m django startapp ex00
#python3 manage.py runserver