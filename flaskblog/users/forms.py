from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = SelectField('Update Profile Picture',
     choices=[(0, "Choose Profile"),
     ("images1", "Blind Cat"),
      ("images2", "Walking Text Cat"),
    ("images3", "High Five Cat"),
    ("images4", "Watching You Cat"),
    ("images5", "Little Devil Cat"),
    ("images6", "I Hate Mondays Cat"),
    ("images7", "Pretty Pleeease Cat"),
    ("images8", "Holding Breath Cat"),
    ("images9", "Spooky Cat"),
    ("images10", "I See You Cat"),
    ("images11", "I am Art Cat"),
    ("images12", "Smiling Cat"),
    ("images13", "Stay Safe Cat"),
    ("images14", "Not In Mood Cat"),
    ("images15", "Who Are You Cat"),
    ("images16", "Big Surprise Cat"),
    ("images17", "Mona Lisa Cat"),
    ("images18", "I am Cool Cat"),
    ("images19", "Grumpy Cat"),
    ("images20", "I am the Beast Cat"),
    ])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
