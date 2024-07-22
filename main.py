from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def site_launch():
    contex = {
        "link": "Подробнее о туре"
    }
    return render_template("index.html", **contex)

@app.route("/shablon/")
def sablon():
    return render_template("shablon.html")

@app.route("/blog/")
def blog():
    contex = {
        "link": "Купить тур"
    }
    return render_template("blog.html", **contex)

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

# Запуск сайта
app.run()