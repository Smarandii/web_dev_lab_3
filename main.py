from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    """
    Функция, которая рендерит страницу http://localhost:5000/ или http://localhost:5000/home
    """
    return render_template("home.html")


@app.route('/publications')
def publications_page():
    """
    Функция, которая рендерит страницу http://localhost:5000/publications
    """
    publications = [
        {"id": 1, "author": "Имя Автора", "post_title": "Заголовок поста", "post_txt": "Текст поста", "publication_date": "Дата публикации"},
        {"id": 2, "author": "Имя Автора", "post_title": "Заголовок поста", "post_txt": "Текст поста", "publication_date": "Дата публикации"},
        {"id": 3, "author": "Имя Автора", "post_title": "Заголовок поста", "post_txt": "Текст поста", "publication_date": "Дата публикации"}
    ]
    return render_template('publications.html', publications=publications)


