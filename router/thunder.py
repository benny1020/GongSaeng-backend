from flask import Blueprint, request, session
from model import db_module
from model import sql_module
from model import image_module
from model import thunder_dao
import json
from collections import OrderedDict
from datetime import *

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

bp = Blueprint("thunder_bp", __name__, url_prefix='/thunder')

#test
@bp.route("/test",methods=['GET'])
def test():
    return json.dumps(dumper(thunder_dao.thunderDao().getThunder(1)),ensure_ascii=False)

#번개 인덱스를 통해 가져오기
@bp.route("/<int:id>",methods=['GET'])
def get_thunder(id):
    try:
        return json.dumps(dumper(thunder_dao.thunderDao().getThunder(id)),ensure_ascii=False)
    except Exception as e:
        return "400"

# thunder filtering
# region metapolis page order:
@bp.route("/list/<int:page>",methods=['GET'])
def get_thunders_list(page):
    if 'region' and 'metapolis' and 'order' in request.args:
        region = request.args.get('region')
        metapolis = request.args.get('metapolis')

    elif 'page' and 'order' in request.args:
        region = None
        metapolis = None

    else:
        return "400"

    order = request.args.get('order')
    dao = thunder_dao.thunderDao()
    thunderList = []
    for th in dao.getThunders(region,metapolis,page,order):
        thunderList.append(dumper(th))

    return json.dumps(thunderList,ensure_ascii=False)


#번개 만들기
@bp.route("",methods=['POST'])
def post_thunder():
    th = thunder_dao.Thunder()
    dao = thunder_dao.thunderDao()
    # 이미지 처리
    if 'image' in request.files:
        contents_image_url = image_module.save_image(request.files.getlist("image"))
        th.contents_image = image_module.url_to_db(contents_image_url)

    try:
        th.setThunderRequest(request.args)
        dao.insertThunder(th)

        return "200"
    except Exception as e:
        return "400"

#번개 리스트 가져오기
@bp.route("/page/<int:page_num>",methods=['GET'])
def get_thunders(page_num):
    dao = thunder_dao.thunderDao()
    thunderList = []
    for th in dao.getThunderList(page_num):
        thunderList.append(dumper(th))

    return json.dumps(thunderList,ensure_ascii=False)

#번개 참여 및 취소하기
@bp.route("/<id>",methods=['POST'])
def get_thundessr(id):
    return "post"