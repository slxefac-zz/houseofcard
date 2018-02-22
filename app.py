from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from datetime import datetime

app = Flask(__name__)

app.config.from_pyfile('config.py')
heroku = Heroku(app)
db = SQLAlchemy(app)
from views import *

if __name__ == "__main__":
    app.run()
