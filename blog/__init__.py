from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.config["SECRET_KEY"] = '5bfd3baa68781953ebfeab00'
db = SQLAlchemy(app)

from blog import routes
