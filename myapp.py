from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/change")
def change():
    return "i made a change !"


if __name__ == "__main__":
    app.run(debug=True)
