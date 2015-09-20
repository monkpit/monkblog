#! /usr/bin/env python

from __future__ import division, print_function, absolute_import
import os

from flask import Flask, send_from_directory, request, \
                    render_template, url_for, redirect

from settings import APP_STATIC, DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

@app.route('/')
def hello_world():
    return render_template('mysite/main.html')

@app.errorhandler(404)
def page_not_found(e):
        return send_from_directory('static', '404.html'), 404

#@app.route('/markdown/<filename>')
def markdown(filename):
    if ".md" not in filename:
        filename += ".md"

    markdown_theme = request.args.get('theme', 'spacelab')

    markdown_content = "# No content provided. #"
    try:
        markdown_content = open(os.path.join(APP_STATIC, 'markdown', filename)).read()
    except IOError:
        markdown_content = "# " + filename + " was not found.#"
    return render_template('mysite/markdown.html',
                            context={"markdown_content": markdown_content,
                                     "markdown_theme": markdown_theme})

@app.route('/markdown/<slug>')
def markdown_db(slug):
    from models import Post, Category
    markdown_content = Post.query.filter_by(slug=slug).first().body
    markdown_theme = request.args.get('theme', 'spacelab')
    return render_template('mysite/markdown.html',
                            context={'markdown_content': markdown_content,
                                     'markdown_theme': markdown_theme})

@app.route('/markdown/images/<filename>')
def markdown_image(filename):
    return redirect('/static/markdown/images/' + filename)

if __name__ == "__main__":
    app.run(debug=True)
