#! /usr/bin/env python

from monkblog.app import app

def register_blueprints(flask_app, parent_modules):
    from flask import Blueprint
    for parent_module in parent_modules:
        imported_module = __import__(parent_module, globals(), locals(), ['object'], -1)
        blueprints = [cls for name, cls
                        in imported_module.__dict__.items()
                        if isinstance(cls, Blueprint)]
        for blueprint in blueprints:
            flask_app.register_blueprint(blueprint)

register_blueprints(app, ['monkblog.blueprints'])

if __name__ == "__main__":
    app.run(debug=True)
