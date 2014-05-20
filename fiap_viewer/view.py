#!/usr/bin/env python
# coding:utf-8
#
# view.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-19
#

from fiap_viewer import app, db
from fiap_viewer.model import PointID
from fiap_viewer.config import wsdl_url
from flask import render_template, request, jsonify
from flask.ext.admin import Admin, AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView

from datetime import datetime, timedelta
from pytz import timezone

from pyfiap.fiap import APP

fiap_app = APP(wsdl_url)

@app.route('/')
def index():
  point_ids = PointID.query.all()
  
  now = datetime.now()
  return render_template("mainpage.html",
    point_ids = point_ids)

@app.route('/PointID/<path:point_id_>')
def point_id(point_id_):
  point_id = PointID.query.filter_by(point_id=point_id_).first()
  return render_template("pointidpage.html",
    point_id = point_id)

@app.route('/FIAPGW')
def fiapgw() :
  point_ids = request.args.get('point_ids', '')
  start = request.args.get('start', '')
  end = request.args.get('end', '')
  
  result = fiap_app.fetch_by_time(point_ids, start, end)

  return jsonify(result=result)

class HomeView(AdminIndexView):
  @expose('/')
  def index(self):
    return self.render('admin/home.html')

admin = Admin(app, index_view=HomeView(name='Home'))
admin.add_view(ModelView(PointID, db.session))
