from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisIsATestSecretKey3'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Data', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Data(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Test, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Data('{self.title}', '{self.date_added}')"


data = [
    {
        'student': 'Miles Morales',
        'company': 'Hooli',
        'salary': '$100,000',
        'position': 'Database Engineer',
        'date_employed': 'August 23, 2019'
    },
    {
        'student': 'Cavin F.H.Y.Z.C.I.T.C.J.C.J.S.-M',
        'company': 'Pied Piper',
        'salary': '$120,000',
        'position': 'Full Stack Scratch Developer',
        'date_employed': 'April 20, 2019'
    }

]
