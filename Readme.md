# Chool management sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/danalvin/Kilimo-High-School.git
$ cd Kilimo-High-School
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.

In order to test the full functionalities, create a superuser model
`python manage.py createsuperuser`, fill in the account details iand log in, the admin panel has all the models and the relations to it and the mainpage of the website has the independent urls,
I have pushed the database and the schema for easier configration
