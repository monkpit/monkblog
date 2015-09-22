from flask import Flask

from monkblog.settings import APP_STATIC, DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
