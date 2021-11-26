from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from blog.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Пользователь с таким именем уже существует!")

    def validate_email_address(self, email_address):
        email = User.query.filter_by(email_address=email_address.data).first()
        if email:
            raise ValidationError("Данная электронная почта уже зарегистрирована!")

    username = StringField(label='Имя пользователя:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Электронная почта:', validators=[Email(message="Введён неверный адресс электронной почты!")])
    password1 = PasswordField(label='Пароль:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Повторите Пароль:', validators=[EqualTo('password1', message="Пароли не совпадают!"), DataRequired()])
    date_of_birth = DateField(label='Дата рождения:', validators=[DataRequired()])
    submit = SubmitField(label='Создать аккаунт')


class LoginForm(FlaskForm):
    username = StringField(label='Имя пользователя:', validators=[DataRequired()])
    password = PasswordField(label='Пароль:', validators=[DataRequired()])
    submit = SubmitField(label='Войти')


class NewPublicationForm(FlaskForm):
    def validate_tags(self, tags):
        try:
            t = tags.split(" ")
            if len(t) != tags.count("#"):
                raise ValidationError("В начале каждого тега должен быть хэштег")
        except Exception:
            raise ValidationError("Тэги должны быть введены через запятую, в начале каждого тега должен быть хэштег")

    post_title = StringField(label='Заголовок публикации', validators=[DataRequired()])
    post_txt = StringField(label='Текст публикации', validators=[DataRequired()])
    tags = StringField(label="Тэги", validators=[DataRequired()])
    submit = SubmitField(label="Создать")
