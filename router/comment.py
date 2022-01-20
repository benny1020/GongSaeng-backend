from flask import Blueprint,request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict
from datetime import *



bp = Blueprint('comment_bp', __name__, url_prefix='/comment')

@bp.route("/read_comment",methods=['GET'])
def read_comment():
    if request.method == 'GET':
        parent_num = str(request.args.get('parent_num'))
        page = request.args.get('page',type=int)
        func = sql_module.sql_func()
        res = func.get_comment(parent_num,page)

        data = []

        for i in range(len(res)):
            js = OrderedDict()
            js["nickname"] = res[i]["m_nickname"]
            js["contents"] = res[i]["co_contents"]
            js["time"] = res[i]["co_regdate"]
            js["profile_image_url"] = func.get_user_image_url(res[i]["m_id"])
            data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj








@bp.route("/write_comment",methods=['POST'])
def write_comment():
    if request.method == 'POST':
        parent_num = request.args.get('parent_num')
        contents = request.args.get('contents')
        time = datetime.strptime(request.args.get('time'), '%Y-%m-%d %H:%M:%S')
        func = sql_module.sql_func()
        func.write_comment(parent_num, session['id'],session['nickname'],contents,time)
        func.increase_comment_num(parent_num)
        comment_num = func.get_comment_num(parent_num)
        js=OrderedDict()
        js["count"]=comment_num
        return js
