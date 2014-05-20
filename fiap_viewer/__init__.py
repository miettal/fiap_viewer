#!/usr/bin/env python
# coding:utf-8
#
# __init__.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-19
#

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import fiap_viewer.config

#flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = fiap_viewer.config
db = SQLAlchemy(app)

import fiap_viewer.view
import fiap_viewer.model
