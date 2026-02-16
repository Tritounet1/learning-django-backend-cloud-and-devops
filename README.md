# Django backend for learn cloud and python backend basics

Récrire tout au propre et simplifié :

## Django

### Create project

```sh
django-admin startproject mysite djangotutorial
```

This will create a directory djangotutorial with a project called mysite inside. The directory name doesn’t matter to Django; you can rename it to anything you like. If it didn’t work, see Problems running django-admin.

Let’s look at what startproject created:

```
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

mysite/: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
```

### Run project dev

```sh
source mon_env/bin/activate
cd mysite
python manage.py runserver
```

### Project vs App

Now that your environment – a “project” – is set up, you’re set to start doing work.

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

### Create app

```sh
python manage.py startapp polls
```

### Polls View

The file polls/views.py :

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

This is the most basic view possible in Django. To access it in a browser, we need to map it to a URL - and for this we need to define a URL configuration, or “URLconf” for short. These URL configurations are defined inside each Django app, and they are Python files named urls.py.

To define a URLconf for the polls app, create a file polls/urls.py with the following content:

```py
from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
]
```

The next step is to configure the root URLconf in the mysite project to include the URLconf defined in polls.urls. To do this, add an import for django.urls.include in mysite/urls.py and insert an include() in the urlpatterns list, so you have:

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path("polls/", include("polls.urls")),
  path("admin/", admin.site.urls),
]
```

The path() function expects at least two arguments: route and view. The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

```sh
python manage.py migrate
```

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies.

If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

These concepts are represented by Python classes. Edit the polls/models.py file so it looks like this:

```py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### Migration

```sh
(mon_env) ➜  mysite git:(main) ✗ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
(mon_env) ➜  mysite git:(main) ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

There’s a command that will run the migrations for you and manage your database schema automatically - that’s called migrate, and we’ll come to it in a moment - but first, let’s see what SQL that migration would run. The sqlmigrate command takes migration names and returns their SQL:

```sh
(mon_env) ➜  mysite git:(main) ✗ python manage.py sqlmigrate polls 0001
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

### Access to interractive shell :

```sh
(mon_env) ➜  mysite git:(main) ✗ python manage.py shell
14 objects imported automatically (use -v 2 for details).

Python 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
NameError: name 'Questions' is not defined. Did you mean: 'Question'?
>>> Question
<class 'polls.models.Question'>
>>> Question.objects.all()
<QuerySet []>
```

### Make the poll app modifiable in the admin

But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this:

```py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### Create admin identifier

```sh
(mon_env) ➜  mysite git:(main) ✗ python manage.py createsuperuser
Username: admin
Email address: admin@gmail.com
Password:
Password (again):
The password is too similar to the username.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

### Access to admin pannel

`localhost:8000/admin`

### Run test

```sh
python manage.py test polls
```

### Modify dependencies

```sh
pip install ...
```

### Update requirements.txt

```sh
pip freeze > requirements.txt
```

### Install dependencies

```sh
pip install -r requirements.txt
```

## Links

- [Install postgresql database for django](https://docs.djangoproject.com/en/6.0/topics/install/#database-installation)
- [Tuto django](https://docs.djangoproject.com/en/6.0/intro)
