from flask import Blueprint, request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict



bp = Blueprint('profile_bp',__name__,url_prefix='/profile')

@bp.route("/edit",methods=['POST'])
def profileEdit():
    if request.method == 'POST':
        nickname = request.args.get('nickname')
        job = request.args.get('job')
        profile = request.args.get('profile')
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





#@bp.route("/profile/post",methods=['GET'])




#@bp.route("/profile/comment", methods=['GET'])
