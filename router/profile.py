from flask import Blueprint, request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict
from datetime import *



bp = Blueprint('profile_bp',__name__,url_prefix='/profile')

@bp.route("/edit",methods=['POST'])
def profileEdit():
    if request.method == 'POST':
        nickname = request.args.get('nickname')
        job = request.args.get('job')
        profile = request.args.get('profile')
        # 이미지 안바꾸는 경우
        profile_image_url = request.args.get('profile_image_url')

        func = sql_module.sql_func()
        func.profile_edit(nickname,job,profile,profile_image_url,session['id'])
        return "true"







@bp.route("/account_manage",methods=['POST'])
def account_manage():
    if request.method == 'POST':
        name = request.args.get('name')
        mail = request.args.get('mail')
        phone = request.args.get('phone')
        func = sql_module.sql_func()
        func.account_edit(name,mail,phone,session['id'])
        return "true"






@bp.route("/pass_change",methods=['POST','GET'])
def pass_change():
    #print(session['id'])
    #return "flas"
    #return session['id']
    if request.method=='POST':
        user_pass = request.args.get('pass')
        func = sql_module.sql_func()
        #print(session['id'])
        func.change_password(session['id'],user_pass)
        return "true"

@bp.route("/mypost", methods=['GET'])
def mypost():
    if request.method=='GET':
        func = sql_module.sql_func()
        user_id = session['id']
        res = func.get_community_post_id(user_id)
        data = []
        for i in range(len(res)):
            js = OrderedDict()
            js['title'] = res[i]['b_title']
            js['board_name'] = func.get_community_name(res[i]['bc_code'])
            js['time'] = res[i]['b_regdate']
            js['comment_num'] = res[i]['b_cnt']
            js['post_index'] = res[i]['b_idx']
            data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj

@bp.route("/mycomment", methods=['GET'])
def mycomment():
    if request.method == 'GET':
        func = sql_module.sql_func()
        user_id = session['id']
        res = func.get_comment_byid(user_id)

        data = []

        for i in range(len(res)):
            js = OrderedDict()
            js['title'] = res[i]['co_contents']
            js['board_name'] = func.get_community_name_byidx(res[i]['b_idx'])
            js['time'] = res[i]['co_regdate']
            js['post_index'] = res[i]['b_idx']
            data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj












#@bp.route("/profile/post",methods=['GET'])




#@bp.route("/profile/comment", methods=['GET'])
