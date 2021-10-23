mock-api
========

Provide an API to service mock data, create new entries and list/detail existing ones. Since the login credentials won't be used, the Deleting faculty won't be provided.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/cookiecutter/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Design Decitions
--------
The intention of this project is to quickly provide an API to show about 15.000 entries,
for this reason was implemented on top of a cookiecutter template, this way I can get a project
base I could work in.

The app was built entirely in docker in order to be able to provide compatibility and modularity.

The Data was obtained randomly from ` mockaroo <https://mockaroo.com/>`_ , it is meant to be a list of clients,
where could be listed showing only its ID in the Database and the email. Although some people advise
not to provide DB ID to the user becuase could give information to be attacked, this is an example and
we're not using credentials either.



Basic Commands
--------------

To run the app it is only necessary to have Docker installed and run the following commands::

    $ docker-compose build
    $ docker-compose up

In order to make easier the test of the API, a 15K entries is provided, run the following commands
to load the DB with it::
    $ docker-compose run --rm django python manage.py loaddata FAKE_DATA.json.gz

At this stage you would be able to access on your browser to localhost:8000/clients/ and see the
existing set of fake clients. This is possible because Django_rest_framework offers a browsable API.

Feel free to use Postman or any other similar tool.

List clients: GET request on `<localhost:8000/clients/>`_

Retrieve a client: GET request on `<localhost:8000/clients/<Client_id>/>`_

Create a client: POST request on `<localhost:8000/clients/>`_ providing a json with the necessary data:
::
{
    "first_name": "",
    "last_name": "",
    "email": "",
    "driving_licence": "",
    "ip_address": "",
    "city": ""
}

Testing
--------------

You can use Django to run the tests::
    $ docker-compose run --rm django pytest

To run the tests, check your test coverage, and generate an HTML coverage report.::

    $ docker-compose run --rm django coverage run -m pytest
    $ docker-compose run --rm django coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose run --rm django pytest

