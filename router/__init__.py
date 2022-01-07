from flask import Flask,session,request
import json
from collections import OrderedDict
from . import register
from . import login
from . import profile
from . import image
from . import mate
from . import comment
from . import community
from . import notify
from model import db_module
from model import sql_module
from model import image_module


app = Flask(__name__)
app.secret_key='abcde'
app.register_blueprint(register.bp)
app.register_blueprint(login.bp)
app.register_blueprint(profile.bp)
app.register_blueprint(image.bp)
app.register_blueprint(mate.bp)
app.register_blueprint(comment.bp)
app.register_blueprint(community.bp)
app.register_blueprint(notify.bp)
#app.config['db_ip']="18.118.131.221"
#app.config['db_ip']="127.0.0.1"



@app.route('/test',methods=['POST'])
def test():
    if request.method == 'POST':
        func = sql_module.sql_func()
        image_url = 30
        idx = 30
        sql = """update bd_board set image_url = \'%s\' where b_idx = \'%d\'"""%(str(image_url),idx)
        func.sql_db.execute(sql)
        return "true"






    #return request_test(request.args)
    #return res[0]['bd_name']



@app.route('/')
def index():
    if "id" in session:
        data = []
        js = OrderedDict()
        js["id"]=session['id']
        js["name"]=session['name']
        js["gender"]=session['gender']
        if session['job']!="":
            js['job']=session['job']
        js["department"]=session['department']
        js["nickname"]=session['nickname']
        js["birth"]=session['birth']
        if session['job']!="":
            js['job']=session['job']
        js['phone']=session['phone']
        if session['profile']!="":
            js['profile']=session['profile']
        if session['profile_image_url']!="":
            js['profile_image_url']=session['profile_image_url']



        data.append(js)
        obj = json.dumps(data, ensure_ascii = False)
        return obj
    else:
        return "NO"


@app.route('/logout')
def logout():
    session.clear()
    return "OK"
