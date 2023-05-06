# api-project

django rest framework porject:
create a folder in pc: Here it is 
```
django-rest-framework
```
open in vs code in terminal and create a virtual env: 
```
python3 -m venv drenv(venv name)
```
Now activate venv in terminal by, 
```
source drenv/bin/activate(mac)
```
for windows: 
```
drenv/Scripts/activate
```
Need to install django in venv: 
```
pip install django
```
If pip upgrading needed: 
```
pip install --upgrade pip
```
create a project of django by: 
```
django-admin startproject apiproject(project name)
```
```cd apiproject```
 ```
python3 manage.py migrate
 ```
```
python3 mange.py startapp myapp(app name)
```
create a superuser: 
```
python3 manage.py createsuperuser(name,email,password) and app will start in 127.0.0.0/admijn
```
