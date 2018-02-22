from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from datetime import datetime

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifxjznlzzqneza:1a0abda54f0546ff89ca46aa061f5057d6555fe6c8f9bacd1316dce39251de6c@ec2-107-22-175-33.compute-1.amazonaws.com:5432/d7o4ha9lf0e6n0'
heroku = Heroku(app)
db = SQLAlchemy(app)
from views import *

if __name__ == "__main__":
    app.run(debug = True)
