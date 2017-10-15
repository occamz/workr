#!/bin/bash

docker exec -it $(docker ps -aqf "name=workr_web") python manage.py migrate
