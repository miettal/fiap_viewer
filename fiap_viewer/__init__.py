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

import sys
import os

directory = os.path.abspath(os.path.dirname(__file__))
database_url = 'sqlite:///'+directory+'/db/fiap_viewer.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)

import fiap_viewer.view
import fiap_viewer.model
