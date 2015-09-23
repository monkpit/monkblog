import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, backref

from monkblog.models.base import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', backref=backref('posts', lazy='dynamic'))
    slug = Column(String(50), unique=True, nullable=False)
    title = Column(String(255), unique=True, nullable=False)
    passphrase = Column(String(255), nullable=True)
    body = Column(Text)
    pub_date = Column(DateTime)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref=backref('posts', lazy='dynamic'))

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
