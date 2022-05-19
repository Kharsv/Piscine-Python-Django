#!/bin/sh

pip show version
mkdir -p local_lib
python3 -m pip install --target=local_lib git+https://github.com/jaraco/path.git --log install_path.log
python3 my_program.py
