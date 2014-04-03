from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# creates application object and db, then import views module
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models 
 
