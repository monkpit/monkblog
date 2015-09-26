from flask import Flask, send_from_directory, request, Blueprint, \
                    render_template, url_for, redirect, abort

from monkblog.models import Author, Post
from monkblog.database import db

model_blueprint = Blueprint('model_blueprint', __name__, template_folder='templates')

@model_blueprint.route('/authors/<slug>')
def show_author(slug):
    author = db.session.query(Author).filter_by(slug=slug).first()
    if author is None:
        abort(404)
    bootstrap_theme = request.args.get('theme', 'spacelab')
    return render_template('author.html', author=author, bootstrap_theme=bootstrap_theme)

@model_blueprint.route('/posts/<slug>')
def post_from_db(slug):
    bootstrap_theme = request.args.get('theme', 'spacelab')
    post_object = db.session.query(Post).filter_by(slug=slug).first()
    if post_object is None:
        abort(404)
    given_passphrase = request.args.get('passphrase', None)
    if post_object.passphrase is not None:
        # Check if the passwords match
        if post_object.passphrase == given_passphrase:
            return render_template('monkblog/single_post.html',
                                    post=post_object,
                                    bootstrap_theme=bootstrap_theme)
        else:
            abort(401)
    else:
        return render_template('monkblog/single_post.html',
                                post=post_object,
                                bootstrap_theme=bootstrap_theme)
