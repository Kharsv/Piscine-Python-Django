#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip --version
pip install -r requirement.txt
python3 -m django startproject helloproject
cd helloproject
python3 -m django startapp helloworld
python manage.py runserverls
