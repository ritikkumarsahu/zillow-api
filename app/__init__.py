from flask import Flask, render_template

app = Flask(__name__)

from app.routes import views
from app.api import endpoints