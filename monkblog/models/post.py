import datetime

from monkblog.database import db

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
