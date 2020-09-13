from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
