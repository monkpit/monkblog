from flask import Flask

app = Flask(__name__)
from monkblog.blueprints import model_blueprint, site_blueprint
from monkblog.settings import APP_STATIC, DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.register_blueprint(model_blueprint)
app.register_blueprint(site_blueprint)
