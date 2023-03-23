# News App

Url shortener app is a test assessment for Tranio

## Table of Contents

* [Setup](#setup)
* [Documentation](#documentation)
* [Linting & Formatting](#linting-and-formatting)

## Setup
### With Docker

Install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/)

After installation run the following command
```bash
docker-compose up -d --no-deps --build
```

And you are good to go


### Without Docker

*The following setup is for Linux users only*

Create virtual environment

```bash
python3 -m venv venv
```

Activate it

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip3 install -r requirements.txt
```

Create .env and .db.env files.
Set the environment variables. 
Use this command:
```bash
cp .env.example .env
```


Use `migrate` command to create tables and set relationships in your database.

```bash
python3 manage.py migrate
```

or

```bash
django-admin migrate
```

Run
```bash
python3 manage.py runserver
```
And you are good to go

## Documentation

* Link to the [docs](http://127.0.0.1:8000/docs/)
## Linting and Formatting

Linting completed with flake8
```bash
flake8 --ignore=E501 --exclude=venv,docs .
```

Formatting completed with black
```bash
black shortener/
```