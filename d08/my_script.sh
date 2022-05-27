#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip3 --version
pip3 install -r requirement.txt
python3 -m django startproject d08
cd d08
python3 -m django startapp ex00
python3 manage.py runserver