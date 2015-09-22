#! /usr/bin/env python

from __future__ import division, print_function, absolute_import
import os

from monkblog.blueprints import model_blueprint, site_blueprint
from monkblog.settings import APP_STATIC, DATABASE_URI
from monkblog.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.register_blueprint(model_blueprint)
app.register_blueprint(site_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
