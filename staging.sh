#! /bin/bash

cp -ur ./markdown/images/* ./monkblog/static/img/post_img
cp -ur ./monkblog/static/img/post_img/* ./markdown/images

python ./create_posts.py

md2resume resume/kylepittman.md

