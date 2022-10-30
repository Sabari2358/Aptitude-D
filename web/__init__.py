from flask import Flask,render_template
from .PyDMath import year
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2529594d'

from web import route

