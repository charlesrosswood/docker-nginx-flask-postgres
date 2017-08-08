# docker-nginx-flask-postgres
Orchestrated Docker containers for NGINX proxy, Gunicorn serving Python 3.6 Flask app with Postgres

Summary
========

This is a basic "naked" setup for a Flask web app with a PostgreSQL database. Specifically it uses:
   - **Python** *3.6* - to execute the business logic code
   - **Flask** *0.12.2* - for a minimal server framework for Python
   - **Gunicorn** *19.6.0* - to expose the Flask server (rather than the Flask builtin dev server)
   - **PostgreSQL** *9.6* - for the web app database
   - **NGINX** *1.11.3* - as the reverse proxy to expose the web app to the outside world on port `80`
