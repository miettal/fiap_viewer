#!/usr/bin/env python
#
# model.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-19
#

from fiap_viewer import app, db

class PointID(db.Model):
  def __repr__(self):
    return self.name

  def __init__(self, name, point_id, about = None) :
    self.name = name
    self.point_id= point_id
    self.about = about

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, unique=True)
  point_id = db.Column(db.String, nullable=False)
  about = db.Column(db.String)
