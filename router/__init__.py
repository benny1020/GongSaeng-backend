from flask import Flask
from . import register
from . import login
app = Flask(__name__)
app.secret_key='abcde'
app.register_blueprint(register.bp)
app.register_blueprint(login.bp)
#app.config['db_ip']="18.118.131.221"
#app.config['db_ip']="127.0.0.1"
