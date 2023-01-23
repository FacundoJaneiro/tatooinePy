from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/tatooinePy'
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


def create_tables():
    with app.app_context():
        db.create_all()
