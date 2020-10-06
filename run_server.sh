#!/bin/bash

echo "running webserver"
cd /home/pi/workspace/you_against_the_book/yatb_django
python3 manage.py runserver 0.0.0.0:8080