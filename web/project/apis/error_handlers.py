#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. module:: error_handlers
    :platform: Unix, Windows
    :synopsis: The error handlers for the app

.. moduleauthor:: Charles Wood <charles.ross.wood@gmail.com>
"""


import flask


errors = flask.Blueprint('error_handlers', __name__)


@errors.app_errorhandler(404)
def not_found(e):
    response = {
        'error': 'these aren\'t the resources you\'re looking for'
    }
    return flask.Response(response=flask.json.dumps(response), status=404,
                          content_type='application/json')


@errors.app_errorhandler(400)
def bad_request(e):
    response = {
        'error': 'help me Obi Wan, you\'re my only hope'
    }
    return flask.Response(response=flask.json.dumps(response), status=400,
                          content_type='application/json')


@errors.app_errorhandler(401)
def unauthorised(e):
    response = {
        'error': 'we would be honored if you would join us'
    }
    return flask.Response(response=flask.json.dumps(response), status=401,
                          content_type='application/json')


@errors.app_errorhandler(403)
def forbidden(e):
    response = {
        'error': 'try not. Do... or do not. There is no try'
    }
    return flask.Response(response=flask.json.dumps(response), status=403,
                          content_type='application/json')


@errors.app_errorhandler(410)
def gone(e):
    response = {
        'error': 'if there\'s a bright centre to the universe, you\'re on the resource that it\'s '
                 'farthest from'
    }
    return flask.Response(response=flask.json.dumps(response), status=410,
                          content_type='application/json')


@errors.app_errorhandler(405)
def method_not_allowed(e):
    response = {
        'error': 'I\'ve got a bad feeling about this'
    }
    return flask.Response(response=flask.json.dumps(response), status=401,
                          content_type='application/json')


@errors.app_errorhandler(500)
def server_error(e):
    response = {
        'error': 'as if millions of voices suddenly cried out in terror, and were suddenly '
                 'silenced. I fear something terrible has happened'
    }
    return flask.Response(response=flask.json.dumps(response), status=500,
                          content_type='application/json')