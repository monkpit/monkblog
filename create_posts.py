#! /usr/bin/env python

from __future__ import print_function
import os
from datetime import datetime, timedelta
#from monkblog.database import db
from flask.ext.sqlalchemy import SQLAlchemy
from monkblog.app import app

db = SQLAlchemy(app)

from monkblog.models import Author, Post, Category, Base
from monkblog.settings import APP_STATIC


def prime_db(basedir):
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    #Base.session.commit()
    db.session.commit()
    filename1 = os.path.join(basedir, 'markdown', 'atom_line-ending-selector.md')
    filename2 = os.path.join(basedir, 'markdown', 'proposal.md')
    filename3 = os.path.join(basedir, 'markdown', 'build_atom.md')
    try:
        kyle_author = Author(real_name="Kyle Pittman", email="info@monkpit.com", twitter="monkpit")
        post_src = open(filename1).read()
        atomcat = Category(name='Atom Editor')

        oeepost = Post(title='Atom Line Ending Selector',
                        body=post_src,
                        category=atomcat,
                        author=kyle_author,
                        pub_date=datetime.utcnow() - timedelta(days=2))
        post_src2 = open(filename2).read()
        novcat = Category(name='NOV')
        atompost = Post(title='OEE Proposal', body=post_src2, category=novcat, passphrase='N0V', author=kyle_author)
        post_src3 = open(filename3).read()
        build_atom_post = Post(title="Build Atom",
                                body=post_src3,
                                category=atomcat,
                                author=kyle_author,
                                pub_date=datetime.utcnow() - timedelta(days=1))
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
    basedir = os.path.dirname(os.path.abspath(__file__))
    prime_db(basedir)
