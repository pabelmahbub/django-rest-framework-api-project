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
python3 manage.py startapp myapp(app name)
```
create a superuser: 
```
python3 manage.py createsuperuser(name,email,password) and app will start in 127.0.0.0/admijn
```
```
python3 manage.py runserver
```
Now create a model inside out myapp:
a. In root app (apiproject) in settings: add in INSTALLED_APP= ['myapp','rest_framework']
b. in models.py of myapp create a model:
```
from django.db import models
```
```
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.name
```
c. go to admin.py of myapp and regiter this model:
```
from django.contrib import admin
from .models import Contact
# Register your models here.
admin.site.register(Contact)
```
d. close the terminal and open new. 
```
i) cd appproject 
j) python3 manage.py makemigrations [if error occurs: pip install djangorestframework
k)python3 manage.py migrate 
l) python3 manage.py runserver
```
Now we can add items in Model through admin url.
#### To add some data using serializers: 
(https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer):
We created model but it is needed to show in JSON data and serializer will do it for us.
Step 1. inside myapp create a file named setializers.py and add these lines of code:
```
from rest_framework import serializers
from myapp.models import Contact



class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=30)
    
    
    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.title = validated_data.get('title', instance.title)
        instance.email = validated_data.get('email', instance.email)
       
        return instance
```
We add some data through shell.[In terminal]
```
cd apiproject
```
```
python3 manage.py runshell
```
Now copy this code in Notepad and edit according model and run it in terminal:
```
from snippets.models import Snippet [from myapp(app name).models import Contact(model class name)]
from snippets.serializers import SnippetSerializer[from myapp(app name).serializers import ContactSerializer(model class name)]
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
```
```
a = Contact(name= 'Another User', title="My new title", email="anoterhuser@email.com")
a.save()
```
Refresh the Model in admin Ui and a new user is created through shell.
Now want to get data in Json format:
In terminal shell:
```
serializer = SnippetSerializer(snippet) [serializer = ContactSerializer(a)]
```
```
serializer.data
```
content = JSONRenderer().render(serializer.data)
content
```
Output is in JSON format.
#### Now implement functionbased api view:
(https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer):
a) Now in myapp-> views.py paste the following code[got from above link]:
```
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import ContactSerializer
```
And:
```
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        apivar = Contact.objects.all()
        serializer = ContactSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```
b) Now in myapp -> urls.py
```
from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.snippet_list),
]
```
c) Finally add this url in root app(apiproject)
```
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```
Done. ```http://127.0.0.1:8000/myapi/```. We get the JSON data
        
To get dynamic api value: 
Paste the following code in views.py of myapp:
```
@csrf_exempt
def api_detail(request, pk):
    try:
        detailVar = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactSerializer(detailVar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(detailVar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detailVar.delete()
        return HttpResponse(status=204)    
  ```
  And add the following url in urls.py in myapp:
  ```
  urlpatterns = [
    path('myapi/', views.api_list),
    path('apidetails/<int:pk>/', views.api_detail),
]
```
Done. search in browser or Thender client of vs code in GET req: http://127.0.0.1:8000/apidetails/1/
