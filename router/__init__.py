from flask import Flask
from . import register

app = Flask(__name__)
app.secret_key='abcde'
app.register_blueprint(register.bp)
