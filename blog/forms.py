from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import Length,  EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Имя пользователя:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Электронная почта:', validators=[Email()])
    password1 = PasswordField(label='Пароль:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Повторите Пароль:', validators=[EqualTo('password1'), DataRequired()])
    date_of_birth = DateField(label='Дата рождения:', validators=[DataRequired()])
    submit = SubmitField(label='Создать аккаунт')
