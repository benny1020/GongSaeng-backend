from flask import Flask,session
import json
from collections import OrderedDict
from . import register
from . import login
from . import profile
from . import image
from . import mate
from . import comment

app = Flask(__name__)
app.secret_key='abcde'
app.register_blueprint(register.bp)
app.register_blueprint(login.bp)
app.register_blueprint(profile.bp)
app.register_blueprint(image.bp)
app.register_blueprint(mate.bp)
app.register_blueprint(comment.bp)
#app.config['db_ip']="18.118.131.221"
#app.config['db_ip']="127.0.0.1"

@app.route('/')
def index():
    if "id" in session:
        data = []
        js = OrderedDict()
        js["id"]=session['id']
        js["name"]=session['name']
        js["gender"]=session['gender']
        js["mail"]=session['mail']
        js["department"]=session['department']
        js["nickname"]=session['nickname']
        js["birth"]=session['birth']
        js['job']=session['job']
        js['phone']=session['phone']
        js['profile']=session['profile']

        data.append(js)
        obj = json.dumps(data, ensure_ascii = False)
        return obj
    else:
        return "NO"
