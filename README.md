# api-project

django rest framework porject:
1) create a folder in pc: Here it is ```django-rest-framework```
2) open in vs code in terminal and create a virtual env: ```python3 -m venv drenv```(venv name)
3) Now activate venv in terminal by, ```source drenv/bin/activate```(mac) for windows: ```drenv/Scripts/activate```
4) Need to install django in venv: ```pip install django```
5) If pip upgrading needed: ```pip install upgrade --upgrade pip```
6) create a project of django by: ```django-admin startproject apiproject```(project name)
7) cd apiproject
8) ```python3 manage.py migrate```
9) ```python3 mange.py startapp myapp```(app name)
10)create a superuser: ```python3 manage.py createsuperuser```(name,email,password) and app will start in 127.0.0.0/admijn
