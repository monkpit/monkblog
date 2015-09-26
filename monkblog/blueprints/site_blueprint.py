from flask import Flask, send_from_directory, request, Blueprint, \
                    render_template, url_for, redirect, abort, make_response
import os
from datetime import datetime, timedelta

from monkblog.models import Post, Author
from monkblog.database import db
from monkblog.app import app
from monkblog.settings import APP_STATIC

site_blueprint = Blueprint('site_blueprint', __name__, template_folder='templates')

@site_blueprint.route('/')
def post_index():
    post_objects = db.session.query(Post).filter_by(passphrase=None).order_by(Post.pub_date.desc()).limit(10).all()
    bootstrap_theme = request.args.get('theme', 'spacelab')
    return render_template('monkblog/post_index.html', posts=post_objects, bootstrap_theme=bootstrap_theme)

@site_blueprint.route('/sitemap.xml')
def sitemap():
    pages=[]
    ten_days_ago=(datetime.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments)==0:
            pages.append(
                       [rule.rule,ten_days_ago]
                       )

    # author model pages
    authors = db.session.query(Author).order_by(Author.slug).all()
    for author in authors:
        url = url_for('model_blueprint.show_author',slug=author.slug)
        pages.append([url])

    # post model pages
    posts = db.session.query(Post).order_by(Post.pub_date).all()
    for post in posts:
        url=url_for('model_blueprint.post_from_db',slug=post.slug)
        pages.append([url])

    # static files
    for current_dir, subdirs, filenames in os.walk(APP_STATIC):
        for filename in filenames:
            relative_file = os.path.join(current_dir, filename).replace(APP_STATIC + os.path.sep, '').replace('\\', '/')
            pages.append([url_for('static', filename=relative_file)])

    sitemap_xml = render_template('base/sitemap.xml', pages=pages)
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

@site_blueprint.route('/images/<filename>')
@site_blueprint.route('/posts/images/<filename>')
def post_image(filename):
    return redirect('/static/img/post_img/' + filename)

@site_blueprint.errorhandler(404)
def page_not_found(e):
        return send_from_directory('static', '404.html'), 404
