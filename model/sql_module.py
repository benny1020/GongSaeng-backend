from datetime import *
import json
from flask import Flask, request, session
from collections import OrderedDict
import numpy as np
import pymysql
from . import db_module

host = '18.118.131.221'
db_id='benny'
pw='benny'
db_name='bappy'

class sql_func():
    def __init__(self):
        self.sql_db = db_module.Database()

    def idCheck(self,user_id):
        sql = """select * from bd_member where m_id =\'%s\'"""%(user_id)
        if(len(self.sql_db.executeAll(sql)) == 0):
            return "true"
        else:
            return "false"

    def nicknameCheck(self, user_nickname):
        sql ="""select * from bd_member where m_nickname = \'%s\'"""%(user_nickname)
        if(len(self.sql_db.executeAll(sql))==0):
            return "true"
        else:
            return "false"

    def loginCheck(self,user_id):
        sql = """select * from bd_member where m_id = \'%s\'"""%(user_id)
        return self.sql_db.executeAll(sql)

    def change_password(self, user_id ,user_pass):
        sql = """ update bd_member set m_pass = \'%s\' where m_id = \'%s\'
        """%(user_pass,user_id)
        self.sql_db.execute(sql)

    def account_edit(self, user_name, user_mail, user_phone, user_id):
        sql = """update bd_member set m_name = \'%s\', m_mail = \'%s\', m_phone = \'%s\' where m_id = \'%s\'
        """%(user_name, user_mail, user_phone, user_id)
        self.sql_db.execute(sql)

    def profile_edit(self, nickname, job, profile, profile_image_url,user_id):
        sql = """update bd_member set m_nickname = \'%s\', m_job = \'%s\', m_profile = \'%s\', profile_image_url = \'%s\' where m_id = \'%s\'
        """%(nickname, job, profile, profile_image_url,user_id)
        self.sql_db.execute(sql)

    def get_mate_list(self, department):
        sql = """select * from bd_member where m_department = \'%s\'"""%(department)
        return self.sql_db.executeAll(sql)

    def get_comment(self, parent_num):
        sql = """select * from bd_comment where b_idx = \'%s\'"""%(parent_num)
        return self.sql_db.executeAll(sql)

    def get_user_image_url(self, user_id):
        sql = """ select profile_image_url from bd_member where m_id = \'%s\'"""%(user_id)
        return self.sql_db.executeAll(sql)[0]['profile_image_url']

    def write_comment(self, parent_num,user_id, user_nickname, contents, time):
        idx = comment_last_idx()+1
        sql = """insert into bd_comment(co_idx, b_idx, m_id, m_nickname, co_contents, co_regdate)
            values('%s','%s','%s','%s','%s','%s')
        """%(idx,parent_num,user_id,user_nickname,contents, time)
        self.sql_db.execute(sql)

    def get_notice_list(self, department):
        sql = """select * from notice_list where department = \'%s\'"""%(department)
        return self.sql_db.executeAll(sql)

    def get_community_index(self):
        sql = """select count(*) as cnt from notice_list"""
        notice_count = self.sql_db.executeAll(sql)
        notice_count = notice_count[0]['cnt']
        sql = """select count(*) as cnt from bd_board"""
        board_count = self.sql_db.executeAll(sql)
        board_count = board_count[0]['cnt']
        return notice_count + board_count

    def get_community_post(self,code):
        sql = """select * from bd_board where bc_code = \'%s\'"""%(code)
        return self.sql_db.executeAll(sql)

    def get_community_post_id(self, user_id):
        sql = """select * from bd_board where m_id = \'%s\'"""%(user_id)
        return self.sql_db.executeAll(sql)

    def get_gather_status(self):
        sql = """select * from bd_together """
        return self.sql_db.executeAll(sql)

    def get_comment_num(self, b_idx):
        sql = """select count(*) as cnt from bd_comment where b_idx = %s"""%(b_idx)
        return self.sql_db.executeAll(sql)[0]['cnt']

    def get_market_info(self):
        sql = """select * from bd_market """
        return self.sql_db.executeAll(sql)

    def increase_comment_num(self, b_idx):
        sql = """ update bd_board set b_cnt = b_cnt + 1 where b_idx = \'%s\'"""%(b_idx)
        self.sql_db.execute(sql)

    def get_community_name(self, b_code):
        sql = """select bd_name from bd_list where bd_code = \'%s\'"""%(b_code)
        return self.sql_db.executeAll(sql)[0]['bd_name']

    def get_comment_byid(self,user_id):
        sql = """select * from bd_comment where m_id = \'%s\'"""%(user_id)
        return self.sql_db.executeAll(sql)

    def get_community_code_byidx(self, parent_num):
        sql = """select * from bd_board where b_idx = \'%s\'"""%(parent_num)
        return self.sql_db.executeAll(sql)[0]['bc_code']

    def get_community_name_byidx(self,idx):
        return self.get_community_name(self.get_community_code_byidx(idx))

    def get_community_post_byidx(self, idx):
        sql = """ select * from bd_board where b_idx = \'%s\'"""%(idx)
        return self.sql_db.executeAll(sql)[0]






    def __del__(self):
        self.sql_db.close()







def comment_last_idx():

    conn = pymysql.connect(host=host, port=3306, user=db_id, password=pw, db=db_name, charset='utf8')
    curs=conn.cursor(pymysql.cursors.DictCursor)
    sql = """select co_idx from bd_comment order by co_idx desc limit 1"""
    curs.execute(sql)

    rows = curs.fetchall()
    #print(rows[0]['co_idx'])
    conn.close()
    return rows[0]['co_idx']

def board_last_idx():

    conn = pymysql.connect(host=host, port=3306, user=db_id, password=pw, db=db_name, charset='utf8')

    curs=conn.cursor(pymysql.cursors.DictCursor)
    sql = """select b_idx from bd_board order by b_idx desc limit 1"""
    curs.execute(sql)

    rows = curs.fetchall()
    #print(rows[0]['b_idx']+1)
    conn.close()
    return rows[0]['b_idx']


def member_last_idx():
    conn = pymysql.connect(host=host, port=3306, user=db_id, password=pw, db=db_name, charset='utf8')
    curs=conn.cursor(pymysql.cursors.DictCursor)
    sql = """select m_idx from bd_member order by m_idx desc limit 1"""
    curs.execute(sql)

    rows = curs.fetchall()
    #print(rows[0]['b_idx']+1)
    conn.close()
    return rows[0]['m_idx']


#comment_last_idx()
#board_last_idx()
