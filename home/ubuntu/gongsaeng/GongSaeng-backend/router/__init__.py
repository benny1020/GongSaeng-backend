from flask import Flask
from . import register
from . import login
app = Flask(__name__)
app.secret_key='abcde'
app.register_blueprint(register.bp)
app.register_blueprint(login.bp)


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
