mock-api
========

Provide an API to service mock data, create new entries and list/detail existing ones. Since the login credentials won't be used, the Deleting faculty won't be provided.

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/cookiecutter/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)

License
:   MIT

Design Decisions
--------
The intention of this project is to quickly provide an API to show about 15.000 entries (virtually there is no limit),
for this reason was implemented on top of a cookiecutter template, this way I can get a project
base I could work on.

Because there is no use of user account or any other credential, The API won't let Update or Delete entries.

The app was built entirely on docker in order to be able to provide compatibility and modularity.
CookieCutter in this case creates 3 containers:
 - Django, for all the necessary logic implemented.
 - PostgreSQL, to store all the data
 - Dosc, this comes on cookiecutter, there were no changes to this.
 - It has the capacity to create and make use of many other tools such as Celety, Redis and more. Although for this solution is no necessary.

Data
-------
The Data was obtained randomly from [Mockaroo](https://mockaroo.com/), it is meant to be a list of clients,
where could be listed showing only its ID in the Database and the email. Although some people advise
not to provide DB ID to the user becuase could give information to be attacked, this is an example and
we're not using credentials either.

Basic Commands
--------------
Make sure you cloned the repo and you are in the root path of the project.

To run the app it is only necessary to have Docker installed and run the following commands:
```
    $ export COMPOSE_FILE=local.yml
    $ docker-compose build
    $ docker-compose up
```
In order to make easier the test of the API, a 15K entries file is provided, run the following command in another terminal
to load the DB with it
```
    $ export COMPOSE_FILE=local.yml
    $ docker-compose run --rm django python manage.py flush
    $ docker-compose run --rm django python manage.py loaddata DATA.json.gz
````

At this stage you would be able to access on your browser to the project's home (http://localhost:8000/),
here you could access to the HTML server side rendered UI to list, retrieve and create clients.


| Actions/Interface | HTML                                  | API                                           |
|-------------------|---------------------------------------|-----------------------------------------------|
| List Clients.     | http://localhost:8000/clients/        | **GET:** http://localhost:8000/api/clients/   |
| Retrieve a Client | http://localhost:8000/clients/1/      | **GET:** http://localhost:8000/api/clients/1/ |
| Create a Client   | http://localhost:8000/clients/create/ | **POST:** http://localhost:8000/api/clients/  |
| Update a Client   | NOT ALLOWED                           | NOT ALLOWED                                   |
| Delete a Client   | NOT ALLOWED                           | NOT ALLOWED                                   |

Feel free to use Postman or any other similar tool.
The data structure to POST to create a client is:
```
{
    "first_name": "",
    "last_name": "",
    "email": "",
    "driving_licence": "",
    "ip_address": "",
    "city": ""
}
```

Testing
--------------

You run the tests using pytest
```
    $ docker-compose run --rm django pytest
```
To run the tests, check your test coverage and generate an HTML coverage report.
```
    $ docker-compose run --rm django coverage run -m pytest
    $ docker-compose run --rm django coverage html
    $ open htmlcov/index.html
```
