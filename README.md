docker
docker-compose

First run:
1) docker-compose build
2) docker-compose up -d
3) docker ps
4) find container id of workr_web
5) docker exec -it IDHERE python manage.py migrate
6) http://127.0.0.1
