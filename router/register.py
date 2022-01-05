from flask import Blueprint,request
from model import db_module
from model import sql_module
import json
from collections import OrderedDict



bp = Blueprint('register_bp', __name__,url_prefix='/register')

@bp.route("",methods=['POST'])
def get_register():
    if request.method == 'POST':
        department = request.args.get('department')
        name = request.args.get('name')
        birth = request.args.get('birth')
        phone = request.args.get('phone')
        user_id = request.args.get('id')
        password = request.args.get('pass')
        nickname = request.args.get('nickname')
        index = sql_module.member_last_idx()+1

        db_class = db_module.Database()
        sql = """insert into bd_member(m_department,m_name,m_birth,
                m_phone,m_id,m_pass,m_nickname,m_idx,approve,profile_image_url)
                values(
                '%s', '%s', '%s', '%s', '%s', '%s','%s', '%d','%d','%s'
                )
        """%(department,name,birth,phone,user_id,password,nickname,int(index),0,"default")
        db_class.execute(sql)
        db_class.db.commit()
        db_class.db.close()
        return "true"

@bp.route("/department",methods=['GET'])
def get_department():
    if request.method == 'GET':
        data = []
        department_list = ["한국장학재단 부산센터","한국장학재단 서울센터","한국장학재단 대구센터","한국장학재단 대전센터","한국장학재단 경기센터","한국장학재단 강원센터","신한은행"]
        department_detail_list = ["부산광역시 연제구 반송로 60", "서울특별시 중구 장충단로6길 54", "대구광역시 중구 명륜로23길 89", "대전광역시 중구 계룡로 843", "경기도 수원시 영통구 광교산로 154-42","강원도 춘천시 강원대학길 1 공과대학 6호관 2층 214호","서울 종로지점"]
        for i in range(len(department_list)):
            js = OrderedDict()
            js["department_name"] = department_list[i]
            js["department_detail"] = department_detail_list[i]
            data.append(js)

        obj = json.dumps(data, ensure_ascii=False)
        return obj
    else:
        return "NO"

@bp.route("/idCheck", methods=['GET'])
def idCheck():
    if request.method == 'GET':
        id = str(request.args.get('id'))
        func = sql_module.sql_func()
        return func.idCheck(id)

@bp.route("/nicknameCheck", methods=['GET'])
def nicknameCheck():
    if request.method == 'GET':
        nickname = request.args.get('nickname')
        func = sql_module.sql_func()
        return func.nicknameCheck(nickname)
