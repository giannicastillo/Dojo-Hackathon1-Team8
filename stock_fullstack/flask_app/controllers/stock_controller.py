from flask_app import app
from flask import render_template, redirect, session, request




@app.route("/stocks")
def stocks():
    return render_template("stocks.html")