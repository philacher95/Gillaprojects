from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, SelectField, PasswordField
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host = "localhost",
    database ="clients",
    user="root",
    password="philacher"
    )

cursor = cnx.cursor()
@app.route("/")
def root():
    return render_template("root.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signupcheck", methods=["POST"])
def check():
    username = str(request.form["username"])
    email = str(request.form["email"])
    password = str(request.form["password"])
    date = request.form["date"]

    cursor = cnx.cursor()

    cursor.execute("INSERT INTO registration(username,email,password,date)VALUES(%s,%s,%s,%s)" ,(username, email, password,date))
    cnx.commit()
    return "<h1>You Have Successfully <em>Registered</em></h1>"



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logincheck", methods = ["POST", "GET"])
def log():
    pass


if __name__ == "__main__":
    app.run(debug=True,host="10.21.244.214")