from flask import Blueprint,request
from model import db_module
from model import sql_module
import json
from collections import OrderedDict



bp = Blueprint('register', __name__,url_prefix='/register')

@bp.route("/")
def register():
    if request.method == 'POST':
        department = request.args.get('department')
        name = request.args.get('name')
        birth = request.args.get('birth')
        phone = request.args.get('phone')
        user_id = request.args.get('id')
        password = request.args.get('pass')
        nickname = request.args.get('nickname')
        index = member_last_idx()+1
        #conn = pymysql.connect(host=host, port=3306, user=id, password=pw, db=db_name, charset='utf8')
        #curs=conn.cursor(pymysql.cursors.DictCursor)

        db_class = db_module.Database()
        sql = """insert into bd_member(m_department,m_name,m_birth,
                m_phone,m_id,m_pass,m_nickname,m_idx)
                values(
                '%s', '%s', '%s', '%s', '%s', '%s','%s', '%d'
                )
        """%(department,name,birth,phone,user_id,password,nickname,int(index))
        db_class.execute(sql)
        db_class.commit()
        db_class.close()
        return "true"

@bp.route("/department")
def get_department():
    if request.method == 'GET':
        data = []
        department_list = ["한국장학재단","진리관","웅비관","신한은행"]
        js = OrderedDict()
        js["department"]=department_list
        data.append(js)
        obj = json.dumps(data, ensure_ascii=False)
        return obj
    else:
        return "NO"

@bp.route("/idCheck")
def idCheck():
    if request.method == 'GET':
        id = request.args.get('id')
