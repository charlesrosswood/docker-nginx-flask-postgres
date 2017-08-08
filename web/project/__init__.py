#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
.. module:: main
    :platform: Unix, Windows
    :synopsis: The app setup file.

.. moduleauthor:: Charles Wood <charles.ross.wood@gmail.com>
"""


import flask

from project.apis import error_handlers
from project.apis import service


app = flask.Flask(__name__, instance_relative_config=True)

# app.config.from_object(__name__)  # sets the config to the variables in this file
app.register_blueprint(error_handlers.errors)  # register the error handlers to the app
app.register_blueprint(service.service, url_prefix='/v1')  # register the password apis
