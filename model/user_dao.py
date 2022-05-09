
from datetime import *
import json
from flask import Flask, request, session
from collections import OrderedDict
import numpy as np
import pymysql
from . import db_module

host = '127.0.0.1'
db_id = 'benny'
pw = 'benny'
db_name = 'bappy'


class User():
    def __init__(self):
        self.idx = 0
        self.id = ""
        self.name = ""
        self.gender = 0
        self.profile = ""
        self.mail = ""
        self.job = ""
        self.birth = ""
        self.phone = ""
        self.department = ""
        self.nickname =""
        self.approve = 1
        self.profile_image_url = ""
        self.thunder = ""

    def setUser(self,res):
        self.idx = res['m_idx']
        self.id = res['m_id']
        self.name = res['m_name']
        self.gender = res['m_gender']
        self.profile = res['m_profile']
        self.mail = res['m_mail']
        self.job = res['m_job']
        self.birth = res['m_birth']
        self.phone = res['m_phone']
        self.department = res['m_department']
        self.nickname = res['m_nickname']
        self.approve = res['approve']
        self.profile_image_url = res['profile_image_url']
        self.thunder = res['m_thunder']


class UserDao():
    def __init__(self):
        self.database = db_module.Database()


    def getUserInfo(self,idx):
        sql = "select * from bd_member where m_idx = '%s'"%(idx)
        res = self.database.executeOne(sql)
        user = User()
        user.setUser(res)
        return user

    def updateUserInfo(self,user):
        sql = """update bd_member set m_thunder = '%s' where m_idx = '%d'
        """%(user.thunder,user.idx)
        self.database.execute(sql)
