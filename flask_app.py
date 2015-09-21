#! /usr/bin/env python

from __future__ import division, print_function, absolute_import
import os

from flask import Flask, send_from_directory, request, \
                    render_template, url_for, redirect, abort

from settings import APP_STATIC, DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

@app.route('/')
def hello_world():
    return render_template('mysite/main.html')

@app.errorhandler(404)
def page_not_found(e):
        return send_from_directory('static', '404.html'), 404

@app.route('/markdown/<slug>')
def markdown_db(slug):
    from models import Post, Category
    post_object = Post.query.filter_by(slug=slug).first()
    given_passphrase = request.args.get('passphrase', None)
    if post_object.passphrase is not None:
        # Check if the passwords match
        if post_object.passphrase == given_passphrase:
            # serve post
            markdown_content = post_object.body
            markdown_theme = request.args.get('theme', 'spacelab')
            return render_template('mysite/markdown.html',
                                    context={'markdown_content': markdown_content,
                                         'markdown_theme': markdown_theme})
        else:
            abort(401)
    else:
        markdown_content = post_object.body
        markdown_theme = request.args.get('theme', 'spacelab')
        return render_template('mysite/markdown.html',
                                context={'markdown_content': markdown_content,
                                     'markdown_theme': markdown_theme})

@app.route('/markdown/images/<filename>')
def markdown_image(filename):
    return redirect('/static/markdown/images/' + filename)

if __name__ == "__main__":
    app.run(debug=True)
