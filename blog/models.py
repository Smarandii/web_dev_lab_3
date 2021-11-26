from blog import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Publication(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.String(length=30), nullable=False)
    post_title = db.Column(db.String(length=30), nullable=False)
    post_txt = db.Column(db.String(length=1024), nullable=False)
    publication_date = db.Column(db.String(length=15), nullable=False)
    tags = db.Column(db.String(50))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    date_of_birth = db.Column(db.String(length=10), nullable=False)
    register_date = db.Column(db.String(length=10), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
