## Configuration
Configuration is stored in `.env`, for examples see `.env.examples`
* This project requires python3.9 and sqlite or Postgres(with Docker).

## Installing on a local machine with Docker

See all commands:
```sh
make all
```

Up project:
```sh
make up
```


## Installing on a local machine with venv
* This project requires python3.9 and sqlite or Postgres(with Docker).
* Create and activate your virtual environment

Install requirements:

```sh
python3 -m venv venv
source venv/bin/activate # unix system
pip install -r requirements.txt
cp .env.example .env  # default environment variables
```

```sh
./manage.py migrate
./manage.py createsuperuser
```
Development servers:

```bash
# run django dev server
$ ./manage.py runserver

