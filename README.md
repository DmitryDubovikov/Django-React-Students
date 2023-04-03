# Django-React-Students

## Project description:

This project is 1/2 test assignment and 1/2 pet project for skills development and demonstration.

Lists of students app: .

## Technologies used: 
* Django, 
* Django REST framework, 
* docker, docker-compose for containerization,
* drf-spectacular for swagger docs,
* django-cors-headers,
* React,
* react-bootstrap

## How to run:

Run containers:

    docker-compose build
    docker-compose up

Run in docker:    

    python manage.py migrate

Check main page functions:

    http://127.0.0.1:3000/


Check swagger docs for API:

    http://127.0.0.1:8000/api/swagger/docs/