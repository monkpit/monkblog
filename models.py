import datetime

from flask_app import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('posts', lazy='dynamic'))
    slug = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    passphrase = db.Column(db.String(255), nullable=True)
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, author, pub_date=None, passphrase=None):
        self.title = title
        self.author = author
        self.body = body
        self.category = category
        self.slug = title.replace(" ", "_")[:50]
        self.passphrase = passphrase

        if pub_date is None:
            pub_date = datetime.datetime.utcnow()

        self.pub_date = pub_date

    def __repr__(self):
        return "<Post %r>" % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(255), unique=True, nullable=False)
    handle = db.Column(db.String(255), unique=True, nullable=False)
    twitter = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, real_name, handle=None):
        self.real_name = real_name
        self.handle = handle
        if handle is None:
            self.handle = real_name

    def __repr__(self):
        representation = ""
        if self.real_name != self.handle:
            representation = "{name} ({handle})".format(name=self.real_name, handle=self.handle)
        else:
            representation = "{name}".format(name=self.real_name)
        return representation
