from flask import Flask, send_from_directory, request, Blueprint, \
                    render_template, url_for, redirect, abort

from monkblog.models import Author

model_blueprint = Blueprint('model_blueprint', __name__, template_folder='templates')

@model_blueprint.route('/authors/<slug>')
def show_author(slug):
    author = Author.query.filter_by(slug=slug).first_or_404()
    return render_template('author.html', author=author)
