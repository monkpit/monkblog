#! /usr/bin/env python

from __future__ import print_function
import os
#from monkblog.database import db
from flask.ext.sqlalchemy import SQLAlchemy
from monkblog.app import app
db = SQLAlchemy(app)
from monkblog.models import Author, Post, Category, Base
from monkblog.settings import APP_STATIC


def prime_db():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    #Base.session.commit()
    db.session.commit()
    filename1 = os.path.join(APP_STATIC, 'markdown', 'atom_line-ending-selector.md')
    filename2 = os.path.join(APP_STATIC, 'markdown', 'proposal.md')
    filename3 = os.path.join(APP_STATIC, 'markdown', 'build_atom.md')
    try:
        kyle_author = Author(real_name="Kyle Pittman", email="info@monkpit.com", twitter="monkpit")
        post_src = open(filename1).read()
        atomcat = Category(name='Atom Editor')
        oeepost = Post(title='atom', body=post_src, category=atomcat, author=kyle_author)
        post_src2 = open(filename2).read()
        novcat = Category(name='NOV')
        atompost = Post(title='OEE Proposal', body=post_src2, category=novcat, passphrase='N0V', author=kyle_author)
        post_src3 = open(filename3).read()
        build_atom_post = Post(title="Build Atom", body=post_src3, category=atomcat, author=kyle_author)
        db.session.add(kyle_author)
        db.session.add(build_atom_post)
        db.session.add(novcat)
        db.session.add(atompost)
        db.session.add(atomcat)
        db.session.add(oeepost)
        db.session.commit()
    except IOError:
        print("could not find file: %s" % filename)

if __name__=="__main__":
    prime_db()
