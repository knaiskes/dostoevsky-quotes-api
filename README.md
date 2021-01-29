# dostoevsky-quotes-api

# Requirements

- Python 3
- Git (optional)
- Django & djangorestframework

# Quick Setup

## Clone this repository

```
$ git clone git@github.com:KNaiskes/dostoevsky-quotes-api.git
```

## Create and activate Python virtual enviroment

```
$ cd dostoevsky-quotes-api/
$ python -m venv venv
$ source venv/bin/activate
```

## Install dependencies

```
$ pip install -r requirements.txt
```

## Makemigrations and Migrate models

```
$ python manage.py makemigrations
$ python manage.py migrate
```
## Create super user (admin)

```
$ python manage.py createsuperuser
```

## Start development server

```
$ python manage.py runserver
```

Now you can login to admin dashboard at [http://localhost:8000/admin/](http://localhost:8000/admin/)
