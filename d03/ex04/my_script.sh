#!/bin/sh

python3 -m venv django_env
source django_env/bin/activate
python -m pip install Django
python -m pip install psycopg2-binary
pip3 install -r requirement.txt
