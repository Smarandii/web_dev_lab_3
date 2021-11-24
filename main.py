from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


def get_tags():
    publications = Publication.query.all()
    tags = set()
    for p in publications:
        for t in p.tags.split(" "):
            tags.add(t)
    return tags


class Publication(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.String(length=30), nullable=False)
    post_title = db.Column(db.String(length=30), nullable=False)
    post_txt = db.Column(db.String(length=1024), nullable=False)
    publication_date = db.Column(db.String(length=15), nullable=False)
    tags = db.Column(db.String(50))


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    register_date = db.Column(db.String(length=10), nullable=False)


@app.route('/')
@app.route('/home')
def home_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/ или http://localhost:5000/home
    """
    return render_template("home.html")


@app.route('/<username>')
@app.route('/home/<username>')
def username_page(username):
    """
        Функция, которая рендерит страницу http://localhost:5000/<username> или http://localhost:5000/home/<username>
    """
    return render_template("user.html", username=username, users=User.query.all(), publications=Publication.query.all())


@app.route('/publications/')
def publications_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/publications
    """
    return render_template('publications.html', publications=Publication.query.all())


@app.route('/publications/<int:post_id>')
def publication_page(post_id):
    """
        Функция, которая рендерит страницу http://localhost:5000/publications/<int:post_id>
    """
    return render_template('publication.html', post_id=post_id, publications=Publication.query.all())


@app.route('/tags/<tag>')
def tag_page(tag):
    """
        Функция, которая рендерит страницу http://localhost:5000/tags/<tag>
    """
    return render_template('tag.html', tag=tag, publications=Publication.query.all())


@app.route('/tags/')
def tags_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/tags
    """
    tags = get_tags()
    return render_template('tags.html', tags=tags)


@app.route('/login')
def login_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/login
    """
    return render_template('login.html')


@app.route('/register')
def register_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/register
    """
    return render_template('register.html')


