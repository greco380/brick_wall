from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisIsATestSecretKey3'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

posts = [
    {
        'student': 'Miles Morales',
        'company': 'Hooli',
        'salary': '$100,000',
        'position': 'Database Engineer',
        'date_employed': 'August 23, 2019'
    }
    {
        'student': 'Cavin F.H.Y.Z.C.I.T.C.J.C.J.S.-M',
        'company': 'Pied Piper',
        'salary': '$120,000',
        'position': 'Full Stack Scratch Developer',
        'date_employed': 'April 20, 2019'
    }

]
