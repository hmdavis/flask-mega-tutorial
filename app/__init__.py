from flask import Flask

# creates application object then import views module
app = Flask(__name__)
app.config.from_object('config')

from app import views
 
