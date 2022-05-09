from datetime import datetime
from flask import request
import json
from flask import Flask, request, session
from collections import OrderedDict
import numpy as np
import pymysql
from . import db_module
from . import sql_module
from model import image_module
from model import user_dao


import json

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
# nickname, department, email, profile
class Thunder():
    def __init__(self):
        self.writer_nickname=""
        self.writer_image=""
        self.metapolis=""
        self.title=""
        self.contents=""
        self.contents_image=""
        self.meet_time=""
        self.register_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        self.location=""
        self.detail_location=""
        self.location_url=""
        self.participants_image=""
        self.participants_num=0
        self.total_num=0
        self.region=""
        self.thunder_participants=""
        self.participants_department=[]
        self.participants_nickname=[]
        self.participants_mail=[]
        self.participants_profile=[]
        self.status = True

    def setThunder(self,participants_num,thunder_participants,thunder_idx,region,writer_nickname,writer_image,metapolis,title,contents,
                 contents_image,meet_time,
                 register_time, location,
                 detail_location,location_url,
                 participants_image,
                 total_num
                 ):
        #--- 이미지 처리
        self.idx = thunder_idx
        self.region = region
        self.writer_nickname = session['nickname']
        self.writer_image = session['profile_image_url']
        #self.writer_nickname = "benny"
        #self.writer_image = "3"

        self.participants_num = participants_num
        self.metapolis = metapolis
        self.title = title
        self.location_url = location_url
        self.contents = contents
        self.contents_image = contents_image
        self.meet_time = meet_time
        #self.register_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        self.register_time = register_time
        self.location = location
        self.detail_location = detail_location
        if participants_image != None:
            self.participants_image = participants_image
        self.total_num = total_num
        self.thunder_participants=thunder_participants

    def setThunderRequest(self, args):
        self.region = args.get("region")
        #self.writer_nickname = args.get("writer_nickname")
        #self.writer_image = args.get("writer_image")
        #self.writer_nickname = "benny"
        #self.writer_image = "3"
        self.metapolis = args.get("metapolis")
        self.title = args.get("title")
        self.contents = args.get("contents")
        #self.contents_image = args.get("contents_image")
        self.meet_time = args.get("meet_time")
        self.location = args.get("location")
        self.location_url = args.get("location_url")
        self.detail_location = args.get("detail_location")
        self.total_num = args.get("total_num",type=int)
        self.thunder_participants = session['idx']
        self.participants_image = session['profile_image_url']
        self.writer_image = session['profile_image_url']
        self.writer_nickname = session['nickname']



class thunderDao():
    def __init__(self):
        self.db = db_module.Database()

    def updateThunder(self,th):
        sql = """
            update bd_thunder set thunder_participants = '%s' , participants_num = '%d' , participants_image = '%s' where thunder_idx = '%s'
        """%(th.thunder_participants,th.participants_num,th.participants_image,th.idx)
        self.db.execute(sql)


    def insertThunder(self,th):
        thunder_idx = sql_module.sql_func().get_community_index()+1
        sql = """
        insert into bd_thunder(participants_image,thunder_participants,thunder_idx,region,participants_num,writer_nickname, writer_image, metapolis, title, contents,
        contents_image,meet_time,register_time,location,detail_location,location_url,total_num)
        values('%s','%s','%d','%s',%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d)
        """%(th.participants_image,th.thunder_participants,thunder_idx,th.region,0,th.writer_nickname,th.writer_image,th.metapolis,th.title,th.contents,th.contents_image,th.meet_time,
             th.register_time,th.location,th.detail_location,th.location_url,th.total_num)
        self.db.execute(sql)

    # metapolis, title, contents
    # contetents_image, meet_time
    # register_time, location,detail_location
    # location_url, participants_image
    # participants_num, total_nums
    # nickname, department, email, profile
    # 참여자에 writer가 있으면 False 나머지 True
    def getThunder(self,idx):
        sql = """select * from bd_thunder where thunder_idx = %s"""%(idx)
        row = self.db.executeAll(sql)[0]
        th = Thunder()
        th.setThunder(row['participants_num'],row['thunder_participants'],row['thunder_idx'],row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                     row["contents_image"],row["meet_time"],
                     row["register_time"], row["location"],
                     row["detail_location"],row["location_url"],
                     row["participants_image"],row["total_num"])

        th.contents_image = image_module.db_to_url(th.contents_image)
        th.contents_image.pop(0)
        th.meet_time = str(th.meet_time)
        th.register_time = str(th.register_time)
        dao = user_dao.UserDao()
        participants = image_module.db_to_url(row['thunder_participants'])

        if str(session['idx']) in participants:
            th.status = False
        else:
            th.status = True

        for participant in participants:
            user = dao.getUserInfo(participant)
            th.participants_mail.append(user.mail)
            th.participants_department.append(user.department)
            th.participants_nickname.append(user.nickname)
            th.participants_profile.append(user.profile)
        return th

    def getThunderList(self,page):
        sql = """
        select * from bd_thunder order by thunder_idx desc limit %d,%d
        """%((page-1)*15,15)
        rows = self.db.executeAll(sql)
        thunderList = []
        for row in rows:
            th = Thunder()
            th.setThunder(row['participants_num'],row['thunder_participants'],row['thunder_idx'],row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                         row["contents_image"],row["meet_time"],
                         row["register_time"], row["location"],
                         row["detail_location"],row["location_url"],
                         row["participants_image"],row["total_num"])
            th.meet_time = str(th.meet_time)
            th.register_time = str(th.register_time)
            th.contents_image = image_module.db_to_url(th.contents_image)
            th.contents_image.pop(0)

            thunderList.append(th)

        return thunderList



    def getThunders(self,region,metapolis,page,order):
        if region == None and metapolis == None:
            if order == "register":
                sql = """
                    select * from bd_thunder where meet_time  >= '%s' order by register_time asc limit %d,%d;
                    """%((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),(page-1)*15,15))
            else:
                sql = """
                    select * from bd_thunder where meet_time  >= '%s' order by meet_time asc limit %d,%d;
                    """%((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),(page-1)*15,15))
            rows = self.db.executeAll(sql)
            thunderList = []
            for row in rows:
                th = Thunder()
                th.setThunder(row['participants_num'],row['thunder_participants'],row['thunder_idx'],row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                             row["contents_image"],row["meet_time"],
                             row["register_time"], row["location"],
                             row["detail_location"],row["location_url"],
                             row["participants_image"],row["total_num"])
                th.meet_time = str(th.meet_time)
                th.register_time = str(th.register_time)
                if th.participants_num == th.total_num:
                    th.status = False
                else:
                    th.status = True
                thunderList.append(th)

            return thunderList
        else:
            if order == "register":
                if region == metapolis:
                    sql = """
                        select * from bd_thunder where meet_time  >= '%s' and metapolis = '%s' order by register_time asc limit %d,%d;
                        """%((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),metapolis,(page-1)*15,15))

                else:
                    sql = """
                        select * from bd_thunder where meet_time  >= '%s' and region = '%s' and metapolis = '%s' order by register_time asc limit %d,%d;
                        """%((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),region,metapolis,(page-1)*15,15))
            else: # order 마감순
                if region == metapolis:
                    sql = """
                        select * from bd_thunder where meet_time  >= '%s' and metapolis = '%s' order by meet_time limit %d,%d;
                        """%((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),metapolis,(page-1)*15,15))

                else:
                    sql = """
                        select * from bd_thunder where region = '%s' and metapolis = '%s' and meet_time  >= '%s' order by meet_time asc limit %d,%d;
                        """%(region,metapolis,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),(page-1)*15,15)
            rows = self.db.executeAll(sql)
            thunderList = []
            for row in rows:
                th = Thunder()
                th.setThunder(row['participants_num'],row['thunder_participants'],row['thunder_idx'],row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                             row["contents_image"],row["meet_time"],
                             row["register_time"], row["location"],
                             row["detail_location"],row["location_url"],
                             row["participants_image"],row["total_num"])
                th.meet_time = str(th.meet_time)
                th.register_time = str(th.register_time)
                th.contents_image = image_module.db_to_url(th.contents_image)[0]
                if th.participants_num == th.total_num:
                    th.status = False
                else:
                    th.status = True
                thunderList.append(th)

            return thunderList
