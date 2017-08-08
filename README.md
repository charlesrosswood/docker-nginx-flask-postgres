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

The Python web app uses a Flask pattern for the directory structure:

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

with a `virtualenv` setup at the root level for Python 3.6. Note that the `web/project/` folder is 
where the Python application lives. The _runfile_, `./web/run.py`, contains nothing but the `app
.run()` command and doesn't need to be modified. 
 
 The `./web/project/__init_.py` file is where the `app` Flask variable is defined and where 
 [blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) are registered to the app. API 
 endpoints are written in `.py` files in `./web/project/apis/` with blueprints that are 
 registered in `./web/project/__init_.py`.