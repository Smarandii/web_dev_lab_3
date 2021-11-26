import datetime

from blog import app, db
from flask import render_template, redirect, url_for

from blog.forms import RegisterForm
from blog.models import Publication, User


def get_tags():
    publications = Publication.query.all()
    tags = set()
    for p in publications:
        for t in p.tags.split(" "):
            tags.add(t)
    return tags


@app.route('/<username>')
@app.route('/home/<username>')
def username_page(username):
    """
        Функция, которая рендерит страницу http://localhost:5000/<username> или http://localhost:5000/home/<username>
    """
    return render_template("user.html", username=username, users=User.query.all(), publications=Publication.query.all())


@app.route('/')
@app.route('/home')
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


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    """
        Функция, которая рендерит страницу http://localhost:5000/register
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              date_of_birth=f"{form.date_of_birth.data.day}.{form.date_of_birth.data.month}.{form.date_of_birth.data.year}",
                              register_date=f"{datetime.date.today().day}.{datetime.date.today().month}.{datetime.date.today().year}",
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('publications_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(err_msg)
    return render_template('register.html', form=form)