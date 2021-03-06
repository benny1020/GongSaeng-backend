from flask import Blueprint, request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict
from datetime import *


bp = Blueprint('notify_bp', __name__, url_prefix='/notify')
# 해당


@bp.route("/read_notify", methods=['GET'])
def read_notify():
    if request.method == 'GET':
        #return "true"
        func = sql_module.sql_func()
        page = request.args.get('page', type=int, default=1)
        res = func.get_notice_list(session['department'], page)

        data = []
        for i in range(len(res)):
            js = OrderedDict()
            js["title"] = res[i]['title']
            js["contents"] = res[i]['contents']
            js['category'] = res[i]['category']
            js['time'] = res[i]['time']
            if res[i]['image_url'] != None:
                js['image_url'] = res[i]['image_url']
            #if str(res[i]['image_url']).split(',')[0] != "None":
            #    js['image_url']= str(res[i]['image_url']).split(',')
            data.append(js)

        obj = json.dumps(data, ensure_ascii=False)
        return obj
