from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


def create_tables():
    with app.app_context():
        db.create_all()
