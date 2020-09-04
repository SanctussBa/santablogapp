from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.static.quotes import quotes
import random
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():


    quote = random.choice(quotes)

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, quote=quote)


@main.route("/about")
def about():
    quote = random.choice(quotes)
    return render_template('about.html', title='About', quote=quote)
