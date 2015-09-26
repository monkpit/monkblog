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
    markdown_theme = request.args.get('theme', 'spacelab')
    return render_template('author.html', author=author, markdown_theme=markdown_theme)

@model_blueprint.route('/posts/<slug>')
def post_from_db(slug):
    post_object = db.session.query(Post).filter_by(slug=slug).first()
    if post_object is None:
        abort(404)
    given_passphrase = request.args.get('passphrase', None)
    if post_object.passphrase is not None:
        # Check if the passwords match
        if post_object.passphrase == given_passphrase:
            # serve post
            markdown_content = post_object.body
            markdown_theme = request.args.get('theme', 'spacelab')
            return render_template('monkblog/single_post.html',
                                    context={'markdown_content': markdown_content,
                                         'markdown_theme': markdown_theme})
        else:
            abort(401)
    else:
        bootstrap_theme = request.args.get('theme', 'spacelab')
        return render_template('monkblog/single_post.html',
                                post=post_object,
                                bootstrap_theme=bootstrap_theme)
