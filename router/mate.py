from flask import Blueprint,request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict


bp = Blueprint('mate_bp', __name__,url_prefix='/mate')

@bp.route("",methods=['GET'])
def get_mate_list():
    if request.method == 'GET':
        department = session['department']
        func = sql_module.sql_func()
        res = func.get_mate_list(department)

        data = []
        for i in range(len(res)):
            js = OrderedDict()
            js["name"] = res[i]["m_name"]
            js["job"] = res[i]["m_job"]
            js["mail"] = res[i]["m_mail"]
            js["profile"] = res[i]["m_profile"]
            js["profile_image_url"] = res[i]["profile_image_url"]
            data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj
