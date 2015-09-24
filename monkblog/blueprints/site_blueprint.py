from flask import Flask, send_from_directory, request, Blueprint, \
                    render_template, url_for, redirect, abort
import os

from monkblog.models import Post, Category
from monkblog.database import db

site_blueprint = Blueprint('site_blueprint', __name__, template_folder='templates')

@site_blueprint.route('/')
def post_index():
    post_objects = db.session.query(Post).filter_by(passphrase=None).order_by(Post.pub_date.desc()).limit(10).all()
    markdown_theme = request.args.get('theme', 'spacelab')
    rendered_posts = [render_template('mysite/partial_post.html', context={'post': post, 'markdown_theme': markdown_theme}) for post in post_objects]
    return render_template('mysite/post_index.html', context={'rendered_posts': rendered_posts})

@site_blueprint.errorhandler(404)
def page_not_found(e):
        return send_from_directory('static', '404.html'), 404
