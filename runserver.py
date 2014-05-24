#!/usr/bin/env python
# coding:utf-8
#
# runserver.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-19
#

from fiap_viewer import app
from fiap_viewer import db
#from fiap_viewer.model import PointID

if __name__ == '__main__':
  #PointID.query.delete()
  db.create_all()

  app.run(debug=True)

