from flask import Blueprint, request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict



bp = Blueprint('profile_bp',__name__,url_prefix='/profile')

#@bp.route("/profile/edit",methods=['POST'])





#@bp.route("/profile/account_manage",methods=['POST'])




@bp.route("/pass_change",methods=['POST'])
def pass_change():
    if request.method=='POST':
        user_pass = request.args.get('pass')
        func = sql_module.sql_func()
        #print(session['id'])
        func.change_password(session['id'],user_pass)
        return "true"





#@bp.route("/profile/post",methods=['GET'])




#@bp.route("/profile/comment", methods=['GET'])
