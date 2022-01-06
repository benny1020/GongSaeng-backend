from flask import Blueprint,request, session
from model import db_module
from model import sql_module
import json
from collections import OrderedDict
from datetime import *

bp = Blueprint('community_bp', __name__, url_prefix='/community')

"""
@bp.route("/write_community", methods = ['POST'])
def write_community():
    if request.method == 'POST':
        title = request.args.get('title')
        contents = request.args.get('contents')
        regdate = request.args.get('time')
        code = request.args.get('code')
        if code == 0: # 함께게시판인경우

        elif code == 1: # 장터게시판인경우

        else:  #자유 건의 유저추가 등 나머지
"""

@bp.route("/find_post_by_index", methods = ['GET'])
def find_post_by_index():
    if request.method == 'GET':
        post_index = request.args.get('post_index')
        func = sql_module.sql_func()
        res = func.get_community_post_byidx(post_index)
        data = []
        js = OrderedDict()
        js['title'] = res['b_title']
        js['nickname'] = res['m_name']
        js['contents'] = res['b_contents']
        js['time'] = res['b_regdate']
        js['board_name'] = func.get_community_name(res['bc_code'])
        js['comment_num'] = res['b_cnt']
        js['profile_image_url'] = func.get_user_image_url(res['m_id'])
        if res['image_url'] == None:
            js['contents_images_url'] = "None"
        else:
            js['contents_images_url'] = res['image_url']

        data.append(js)
        obj = json.dumps(data, ensure_ascii = False)
        return obj




#
#
# code 0 함께
# code 1 장터
# code 2 자유
# code 3 건의
# code 4 장터
# code 5 유저추가
@bp.route("/read_community",methods = ['GET'])
def read_community():
    if request.method == 'GET':
        func = sql_module.sql_func()
        code = request.args.get('code')
        res = func.get_community_post(code)
        if code == '0': # 함께 게시판인경우
            gather_status = func.get_gather_status()
            data = []
            for i in range(len(res)):
                js = OrderedDict()
                js['idx'] = res[i]['b_idx']
                js['code'] = res[i]['bc_code']
                js['id'] = res[i]['m_id']
                js['nickname'] = res[i]['m_name']
                js['title'] = res[i]['b_title']
                js['contents'] = res[i]['b_contents']
                js['comment_cnt'] = res[i]['b_cnt']
                js['time'] = res[i]['b_regdate']
                if res[i]['image_url'] == None:
                    js['image_url']="None"
                else:
                    js['image_url'] = res[i]['image_url']
                js['gather_status'] = gather_status[i]['gather_status']
                data.append(js)

        elif code == '1': # 장터 게시판인 경우
            market_info = func.get_market_info()
            #return str(len(market_info))
            data = []
            for i in range(len(res)):
                js = OrderedDict()
                js['idx'] = res[i]['b_idx']
                js['code'] = res[i]['bc_code']
                js['id'] = res[i]['m_id']
                js['nickname'] = res[i]['m_name']
                js['title'] = res[i]['b_title']
                js['contents'] = res[i]['b_contents']
                js['comment_cnt'] = res[i]['b_cnt']
                js['time'] = res[i]['b_regdate']
                if res[i]['image_url'] == None:
                    js['image_url']="None"
                else:
                    js['image_url'] = res[i]['image_url']
                js['price'] = market_info[i]['price']
                js['status'] = market_info[i]['status']
                data.append(js)

        else:   # 나머지 게시판인경우 형식 똑같음
            data = []
            for i in range(len(res)):
                js = OrderedDict()
                js['idx'] = res[i]['b_idx']
                js['code'] = res[i]['bc_code']
                js['id'] = res[i]['m_id']
                js['name'] = res[i]['m_name']
                js['title'] = res[i]['b_title']
                js['contents'] = res[i]['b_contents']
                js['comment_cnt'] = res[i]['b_cnt']
                js['time'] = res[i]['b_regdate']
                if res[i]['image_url'] == None:
                    js['image_url']="None"
                else:
                    js['image_url'] = res[i]['image_url']
                data.append(js)

        obj = json.dumps(data, ensure_ascii = False)
        return obj
