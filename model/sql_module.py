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
        self.sql_db.commit()
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
