from flask import Blueprint, request
from model import db_module
from model import sql_module
import json
from collections import OrderedDict


bp = Blueprint('login_bp',__name__, url_prefix='/login')

@bp.route("/", methods=['POST'])
def login():
    if request.method == 'POST':
        user_id = request.args.get('id')
        user_pass = request.args.get('pass')
        func = sql_module.sql_func()
        rows = func.loginCheck(user_id)
        if len(rows) and (rows[0]['m_pass'] == user_pass) ==0:
            login_num="false"
        else:
            login_num="true"

        if(rows[0]['approve']==0):
            approve_num = "false"
        else:
            approve_num = "true"

        data = []
        js = OrderedDict()
        js['login']=login_num
        js['approve']=approve_num
        data.append(js)
        obj = json.dumps(data,ensure_ascii = False)
        return obj
