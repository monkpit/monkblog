import datetime

from sqlalchemy import Column, Integer, String
from monkblog.models.base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name
