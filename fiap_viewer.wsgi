#!/usr/bin/env python
# coding:utf-8
#
# fiap_viewer.wsgi
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-19
#

import sys
sys.path.insert(0, '/var/www/fiap_viewer')
from fiap_viewer import app as application
from fiap_viewer import db

db.create_all()
application.debug = True
