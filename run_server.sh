#!/bin/bash

cd /home/pi/workspace/you_against_the_book
echo "running webserver"
cd yotams_race
python3 manage.py runserver 0.0.0.0:8080