import datetime

from sqlalchemy import Column, Integer, String

from monkblog.models.base import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    slug = Column(String(255), unique=True, nullable=False)
    real_name = Column(String(255), unique=True, nullable=False)
    handle = Column(String(255), unique=True, nullable=False)
    twitter = Column(String(255))
    email = Column(String(255))

    def __init__(self, real_name, email=None, twitter=None, handle=None):
        self.real_name = real_name
        self.handle = handle
        self.twitter = twitter
        self.email = email
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
