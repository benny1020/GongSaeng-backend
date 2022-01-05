from flask import Blueprint,request
from model import db_module
from model import sql_module
import json
from collections import OrderedDict



bp = Blueprint('comment_bp', __name__, url_prefix='/comment')

@bp.route("/read_comment",methods=['GET'])
def read_comment():
    if request.method == 'GET':
        parent_num = str(request.args.get('parent_num'))
        func = sql_module.sql_func()
        res = func.get_comment(parent_num)

        data = []

        for i in range(len(res)):
            js = OrderedDict()
            js["nickname"] = res[i]["m_nickname"]
            js["contents"] = res[i]["co_contents"]
            js["time"] = res[i]["co_regdate"].strftime('%Y-%m-%d : %H:%m')
            js["profile_image_url"] = func.get_user_image_url(res[i]["m_id"])
            data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj








#@bp.route("/write_comment",methods=['POST'])
#def write_comment():
