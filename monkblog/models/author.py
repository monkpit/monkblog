import datetime
from monkblog.database import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    real_name = db.Column(db.String(255), unique=True, nullable=False)
    handle = db.Column(db.String(255), unique=True, nullable=False)
    twitter = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, real_name, handle=None):
        self.real_name = real_name
        self.handle = handle
        if handle is None:
            self.handle = real_name
        self.slug = self.handle.replace(' ', '')

    def __repr__(self):
        representation = ""
        if self.real_name != self.handle:
            representation = "{name} ({handle})".format(name=self.real_name, handle=self.handle)
        else:
            representation = "{name}".format(name=self.real_name)
        return representation
