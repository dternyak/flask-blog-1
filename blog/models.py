"""These are the models for the blog"""
from datetime import date

from blog import db

class Post(db.Model):
    """
    A post on the blog

    :param int id: ID of this post (KEY)
    :param datetime.date date: Date of this post
    :param str title: Title of this post
    :param str body_md: Markdown version of this post
    :param str body_html: HTML version of this post (generated automatically from markdown)
    :param str css_file: Optional name of the custom css file
    :param str user_email: Email of the user who posted this
    :param User user: User who posted this
    """
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, default=date.today())
    title = db.Column(db.String)
    body_md = db.Column(db.Text)
    body_html = db.Column(db.Text)
    css_file = db.Column(db.String, default=None, nullable=True)
    user_email = db.Column(db.String, db.ForeignKey('user.email'))
    user = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))

    def __str__(self):
        return self.title

class User(db.Model):
    """
    A user of the blog

    :param str email: Email of this user (KEY)
    :param str name: Name of this user
    :param str url: URL of this user
    :param str about_md: Markdown version of user's about section
    :param str about_html: HTML version of user's about section (generated automatically from markdown)
    :param str css_file: Optional name of the custom css file
    :param str password_hash: Hash of this user (bcrypt & salt)
    """
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    about_md = db.Column(db.Text)
    about_html = db.Column(db.Text)
    css_file = db.Column(db.String, default=None, nullable=True)
    password_hash = db.Column(db.String)

    def __str__(self):
        return self.name

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

class Service(db.Model):
    """
    A service for a user

    :param int id: ID of this service (KEY)
    :param str name: Name of this service
    :param str icon_file: Icon file of this service
    :param str alt_text: Optional alt-text for the icon
    :param str css_class: Optional css class of this icon
    :param str user_emal: Email of this service's user
    :param User user: This service's user
    """
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    icon_file = db.Column(db.String)
    alt_text = db.Column(db.String, default=None, nullable=True)
    css_class = db.Column(db.String, default=None, nullable=True)
    user_email = db.Column(db.String, db.ForeignKey('user.email'))
    user = db.relationship('User', backref=db.backref('services', lazy='dynamic'))

    def __str__(self):
        return "{0} @ {1}".format(str(self.user), self.name)

