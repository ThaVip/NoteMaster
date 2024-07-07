from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from app import routes
