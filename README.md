# docker-nginx-flask-postgres
Orchestrated Docker containers for NGINX proxy, Gunicorn serving Python 3.6 Flask app with Postgres

Summary
========

This is a basic "naked" setup for a Flask web app with a PostgreSQL database. Specifically it uses:
   - **Python** _3.6_ - to execute the business logic code
   - **Flask** _0.12.2_ - for a minimal server framework for Python
   - **Gunicorn** _19.6.0_ - to expose the Flask server (rather than the Flask builtin dev server)
   - **PostgreSQL** _9.6_ - for the web app database
   - **NGINX** _1.11.3_ - as the reverse proxy to expose the web app to the outside world on port
    `80`

Usage
=====

Pull this repo by:

```bash
$ git clone git@github.com:charlesrosswood/docker-nginx-flask-postgres.git ./
```

To use this package run:

```bash
$ docker-compose build
$ docker-compose up
```

Then navigate to `0.0.0.0/v1/` to get the default response:
![screenshot of hitting root](http://i.imgur.com/UyAF0Fu.png)

Project setup
=============

The directory structure of the project is:

```bash
.
├── README.md
├── docker-compose.yml
├── nginx
│   ├── Dockerfile
│   ├── nginx.conf
│   └── service.conf
├── postgres
│   └── Dockerfile
|
└── web
    ├── Dockerfile
    ├── necessary_packages.txt
    ├── project
    │   ├── __init__.py
    │   ├── apis
    │   ├── static
    │   └── templates
    ├── requirements.txt
    └── run.py
```

Python Flask + Gunicorn web app container `web/`
------------------------------------------------

The Python web app uses a Flask pattern for the directory structure:
```bash
web
├── Dockerfile
├── necessary_packages.txt
├── project
│   ├── __init__.py
│   ├── apis
│   ├── static
│   └── templates
├── requirements.txt
└── run.py
```

with a `virtualenv` setup at the root level for Python 3.6. Note that the `web/project/` folder is 
where the Python application lives. The _runfile_, `./web/run.py`, contains nothing but the `app
.run()` command and doesn't need to be modified. 
 
The `./web/project/__init_.py` file is where the `app` Flask variable is defined and where 
[blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) are registered to the app. API 
endpoints are written in `.py` files in `./web/project/apis/` with blueprints that are 
registered in `./web/project/__init_.py`.
 
PostgreSQL server container `postgres/`
---------------------------------------

All PostgreSQL database setup scripts should be written in `./postgres/` folder as SQL scripts. 
The Dockerfile at `./postgres/Dockerfile` should then have lines added to copy each SQL script 
into the container's default execution folder (`/docker-entrypoint-initdb.d/`). 

> **NOTE:** SQL scripts in `/docker-entrypoint-initdb.d/` are executed in alphabetical order, so 
> consider naming conventions like `00_<filename>.sql`, `01_<filename>.sql`.

For every SQL script, add a `COPY` line to the Dockerfile:

```dockerfile
COPY <filename1>.sql /docker-entrypoint-initdb.d/00_<filename>.sql
COPY <filename2>.sql /docker-entrypoint-initdb.d/01_<filename>.sql
...
```

The Postgres username and password can be set in the Dockerfile too.

Currently the Postgres database _exposes_ port `5432` to the outside world to allow connections 
outside of the Docker network. This is set in the `./docker-compose.yml` file, currently:

```yaml
...
 postgres:
   restart: always
   build: ./postgres
   volumes_from:
     - data
   ports:
     - "5432:5432"
...
```

to stop exposing port `5432` to the outside world, change it to:

```yaml
...
 postgres:
   restart: always
   build: ./postgres
   volumes_from:
     - data
   expose:
     - "5432"
...
```

NGINX container `nginx/`
------------------------

The NGINX shouldn't need any setup. It listens to the `web` container on port `8000` and exposes 
port `80` (HTTP) and `443` (HTTPS) to the outside world.