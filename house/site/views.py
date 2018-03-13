from app import app, db, render_template
from datetime import datetime
from models import Blogpost

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    titulo = request.form['titulo']
    subtitulo = request.form['subtitulo']
    autor = request.form['autor']
    contenido = request.form['contenido']

    post = Blogpost(title=titulo, subtitle=subtitulo, author=autor, content=contenido, date_posted = datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))
