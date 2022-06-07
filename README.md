In this scenario, this project is an API developed for SoftDesk, a software company, to facilitate the monitoring of projects and problems encountered in their development.

The user can send requests to this API in order to get information about :
  - the projects to which he is a contributor, 
  - the other contributors of the project,
  - the problems related to these projects,
  - comments left on these problems.

This application was built using Django Rest Framework in its version 3.13.1

Objectives of the project:
    - Explore the functioning of an API 
    - Create an API using Django REST framework
    - Create the documentation of an API
    - Secure an application via authentication, permissions, token, etc.

To launch the application, follow the instructions below

## Create virtual environment

From your terminal, enter the following commands depending on your operating system

### From Linux/ MAC OS

    $ python -m venv <environment_name>
    example : python -m venv venvAPI
    
### From Windows:
    
    $ virtualenv <environment_name>
    example : virtualenv venvAPI 
    
## Activate virtual environment

### From Linux / MAC OS:

    $ source <environment_name>/bin/activate
    example : source venvAPI/bin/activate
   
### From Windows:

    $ source <environment_name>/Scripts/activate
    example : source venvAPI/Scripts/activate
    
## Installation of packages : 

    $ pip install -r requirements.txt

## Launch application

    $ python manage.py runserver

## Acces to documentation

You can access to the API documentation [at this address](https://documenter.getpostman.com/view/17414272/UVXnFtu4)