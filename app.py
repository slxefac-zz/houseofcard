from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifxjznlzzqneza:1a0abda54f0546ff89ca46aa061f5057d6555fe6c8f9bacd1316dce39251de6c@ec2-107-22-175-33.compute-1.amazonaws.com:5432/d7o4ha9lf0e6n0'
db = SQLAlchemy(app)

class Blogpost(db.Model):
    __tablename__='post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_poster = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __repr__(self):
        return '<title %r>' % (self.title)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
