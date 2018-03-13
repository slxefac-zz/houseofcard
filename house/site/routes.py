from flask import Blueprint, render_template, url_for, request, redirect
from datetime import datetime
from house import db
from .models import Blogpost
mod = Blueprint('site', __name__, template_folder='templates')

@mod.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('site/index.html', posts=posts)

@mod.route('/about')
def about():
    return render_template('site/about.html')

@mod.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('site/post.html', post=post)

@mod.route('/contact')
def contact():
    return render_template('site/contact.html')

@mod.route('/add')
def add():
    return render_template('site/add.html')

@mod.route('/addpost', methods=['POST'])
def addpost():
    titulo = request.form['titulo']
    subtitulo = request.form['subtitulo']
    autor = request.form['autor']
    contenido = request.form['contenido']
    post = Blogpost(title=titulo, subtitle=subtitulo, author=autor, content=contenido, date_posted = datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('site.index'))
