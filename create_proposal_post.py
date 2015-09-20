#! /usr/bin/env python

from __future__ import print_function
import os
from models import *
from settings import APP_STATIC

def prime_db():
    filename = os.path.join(APP_STATIC, 'markdown', 'proposal.md')
    try:
        post_src = open(filename).read()
        db.drop_all()
        db.create_all()
        novcat = Category(name='NOV')
        oeepost = Post(title='OEE Proposal', body=post_src, category=novcat)
        db.session.add(novcat)
        db.session.add(oeepost)
        db.session.commit()
    except IOError:
        print("could not find file: %s" % filename)

if __name__=="__main__":
    prime_db()
