from flask import Flask, render_template
from tmp import publications, users
app = Flask(__name__)


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
    return render_template("user.html", username=username, users=users, publications=publications)


@app.route('/publications/')
def publications_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/publications
    """
    return render_template('publications.html', publications=publications)


@app.route('/publications/<int:post_id>')
def publication_page(post_id):

    return render_template('publication.html', post_id=post_id, publications=publications)


@app.route('/tags')
def tags_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/tags
    """
    return render_template('tags.html')


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


