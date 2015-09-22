#! /usr/bin/env python

from __future__ import print_function
import os
import monkblog.models as models
from monkblog.settings import APP_STATIC
from monkblog.database import db

def prime_db():
    db.drop_all()
    db.create_all()
    filename1 = os.path.join(APP_STATIC, 'markdown', 'atom_line-ending-selector.md')
    filename2 = os.path.join(APP_STATIC, 'markdown', 'proposal.md')
    try:
        kyle_author = models.Author(real_name="Kyle Pittman")
        post_src = open(filename1).read()
        atomcat = models.Category(name='Atom Editor')
        oeepost = models.Post(title='atom', body=post_src, category=atomcat, author=kyle_author)
        post_src2 = open(filename2).read()
        novcat = models.Category(name='NOV')
        atompost = models.Post(title='OEE Proposal', body=post_src2, category=novcat, passphrase='N0V', author=kyle_author)
        db.session.add(kyle_author)
        db.session.add(novcat)
        db.session.add(atompost)
        db.session.add(atomcat)
        db.session.add(oeepost)
        db.session.commit()
    except IOError:
        print("could not find file: %s" % filename)

if __name__=="__main__":
    prime_db()
