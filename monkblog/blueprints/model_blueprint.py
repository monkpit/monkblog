from flask import Flask, send_from_directory, request, Blueprint, \
                    render_template, url_for, redirect, abort

from monkblog.models import Author
from monkblog.database import db

model_blueprint = Blueprint('model_blueprint', __name__, template_folder='templates')

@model_blueprint.route('/authors/<slug>')
def show_author(slug):
    author = db.session.query(Author).filter_by(slug=slug).first()
    if author is None:
        abort(404)
    markdown_theme = request.args.get('theme', 'spacelab')
    return render_template('author.html', author=author, markdown_theme=markdown_theme)
