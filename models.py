import datetime

from flask_app import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        self.category = category
        self.slug = title.replace(" ", "_")[:50]

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

