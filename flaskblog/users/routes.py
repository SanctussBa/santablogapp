from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm

from flaskblog.users.utils import save_picture
from flaskblog.static.quotes import quotes
import random
users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    quote = random.choice(quotes)
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form, quote=quote)


@users.route("/login", methods=['GET', 'POST'])
def login():
    quote = random.choice(quotes)
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful! Please check email and password!', 'danger')
    return render_template('login.html', title='Login', form=form, quote=quote)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    quote = random.choice(quotes)
    form = UpdateAccountForm()

    #This is picture which shows when you open account page. It is path variable because in HTML this will be as src= "path to image file"
    #it also
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    if form.validate_on_submit(): #When "submit" button is pressed
        if form.picture.data: # and in our html forms is new data about picture
            picture_file = save_picture(form.picture.data) # Create a variable which is executig in function def save_picture(form-picture): in utils.property
            #It takes that new uploaded picture from html form and changes according to save_picture() function
            current_user.image_file = picture_file# now we change current users picture name to newly created picture file name.
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account',
                           image_file=image_file, form=form, quote=quote)


@users.route("/user/<string:username>", methods=['GET', 'POST'])
def user_posts(username):
    quote = random.choice(quotes)
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user, quote=quote)
