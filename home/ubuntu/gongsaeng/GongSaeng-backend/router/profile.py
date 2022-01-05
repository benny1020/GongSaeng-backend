from flask import Blueprint, request
from model import db_module
from model import sql_module
import json
from collections import OrderedDict


bp = Blueprint('profile_bp',__name__.url_prefix='/profile')

@bp.route("/profile/edit",methods=['POST'])





@bp.route("/profile/account_manage",methods=['POST'])
def account_manage():
    if request.method == 'POST':
        user_name = request.args.get('name')
        user_mail = request.args.get('mail')
        user_phone = request.args.get('phone')





@bp.route("/profile/pass_change",methods=['POST'])




@bp.route("/profile/post",methods=['GET'])




@bp.route("/profile/comment", methods=['GET'])
