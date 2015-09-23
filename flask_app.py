#! /usr/bin/env python

from monkblog.app import app
from flask import Blueprint
import importlib, pkgutil

def register_blueprints(flask_app, parent_modules):
    for parent_module in parent_modules:
        loaded_module = importlib.import_module(parent_module)
        blueprint_names = [name for file, name, ispkg in pkgutil.iter_modules(loaded_module.__path__) if ispkg is False]
        for blueprint_name in blueprint_names:
            blueprint_module = importlib.import_module(parent_module + '.' + blueprint_name)
            for cls in [cls for name, cls in blueprint_module.__dict__.items() if isinstance(cls, Blueprint)]:
                flask_app.register_blueprint(cls)

register_blueprints(app, ['monkblog.blueprints'])

if __name__ == "__main__":
    app.run(debug=True)
