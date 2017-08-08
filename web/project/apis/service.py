#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
≈.. module:: main
    :platform: Unix, Windows
    :synopsis: The app setup file.

.. moduleauthor:: Charles Wood <charles.ross.wood@gmail.com>
"""


import flask


service = flask.Blueprint('service', __name__)


@service.route('/', methods=['GET'])
def index():
    return flask.Response(response=flask.json.dumps({'message': 'hello world'}), status=200,
                          headers=None, content_type="application/json;version=0.1")

