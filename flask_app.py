#! /usr/bin/env python

from __future__ import division, print_function, absolute_import
import os

from flask import Flask, send_from_directory, request, \
                    render_template, url_for, redirect, abort

from settings import APP_STATIC, DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

if __name__ == "__main__":
    app.run(debug=True)
