# dostoevsky-quotes-api
A platform to share quotes from Dostoevsky novels

## Demo video
![Video](https://youtu.be/uc_NT4onxnA)

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


## API Routes

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Path</th>
<th scope="col" class="org-left">Parameter</th>
<th scope="col" class="org-left">Request Method</th>
<th scope="col" class="org-left">Data</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">quotes/</td>
<td class="org-left">None</td>
<td class="org-left">GET</td>
<td class="org-left">All available quotes (paginated)</td>
</tr>


<tr>
<td class="org-left">quotes/random</td>
<td class="org-left">None</td>
<td class="org-left">GET</td>
<td class="org-left">A single random quote</td>
</tr>


<tr>
<td class="org-left">quotes/</td>
<td class="org-left">pk</td>
<td class="org-left">GET</td>
<td class="org-left">Single quote based on the given id</td>
</tr>


<tr>
<td class="org-left">quotes/novel/</td>
<td class="org-left">novel</td>
<td class="org-left">GET</td>
<td class="org-left">All quotes based on the given novel (paginated)</td>
</tr>
</tbody>
</table>
