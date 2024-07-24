from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route("/")
def site_launch():
    context = {
        "link": "Подробнее о туре"
    }
    return render_template("index.html", **context)

@app.route("/shablon/")
def sablon():
    return render_template("shablon.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/blog/", methods=["GET", "POST"])
def index():
    context = {
        "link": "Опубликовать пост"
    }
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content': content})
    return render_template('blog.html', posts=posts, **context)
