from flask import Flask

# creates application object then import views module
app = Flask(__name__)
from app import views 
