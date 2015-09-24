from flask import Flask
from flask.ext.misaka import Misaka

from monkblog.settings import APP_STATIC, DATABASE_URI, CONNECTION_POOL_RECYCLE

app = Flask(__name__)
Misaka(app, fenced_code=True)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_POOL_RECYCLE'] = CONNECTION_POOL_RECYCLE
