#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
.. module:: run
    :platform: Unix, Windows
    :synopsis: The app run file.

.. moduleauthor:: Charles Wood <charles.ross.wood@gmail.com>
"""


import os
from project import app


DEBUG = os.getenv('DEBUG', 'True') == 'True'
PORT = os.getenv('PORT', '5000')
HOST = os.getenv('HOST', 'localhost')


if __name__ == '__main__':
    app.run(host=HOST, port=int(PORT), debug=DEBUG)
