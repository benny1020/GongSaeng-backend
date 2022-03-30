from datetime import datetime
from flask import request
import json
from flask import Flask, request, session
from collections import OrderedDict
import numpy as np
import pymysql
from . import db_module

import json

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


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

    def setThunder(self,region,writer_nickname,writer_image,metapolis,title,contents,
                 contents_image,meet_time,
                 register_time, location,
                 detail_location,location_url,
                 participants_image,
                 total_num
                 ):
        self.region = region
        self.writer_nickname = writer_nickname
        self.writer_image = writer_image
        self.metapolis = metapolis
        self.title = title
        self.location_url = location_url
        self.contents = contents
        self.contents_image = contents_image
        self.meet_time = meet_time
        self.register_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        self.location = location
        self.detail_location = detail_location
        if participants_image != None:
            self.participants_image = participants_image
        self.total_num = total_num

    def setThunderRequest(self, args):
        self.region = args.get("region")
        self.writer_nickname = args.get("writer_nickname")
        self.writer_image = args.get("writer_image")
        self.metapolis = args.get("metapolis")
        self.title = args.get("title")
        self.contents = args.get("contents")
        self.contents_image = args.get("contents_image")
        self.meet_time = args.get("meet_time")
        self.location = args.get("location")
        self.location_url = args.get("location_url")
        self.detail_location = args.get("detail_location")
        self.total_num = args.get("total_num",type=int)



class thunderDao():
    def __init__(self):
        self.db = db_module.Database()


    def insertThunder(self,th):
        sql = """
        insert into bd_thunder(region,participants_num,writer_nickname, writer_image, metapolis, title, contents,
        contents_image,meet_time,register_time,location,detail_location,location_url,total_num)
        values('%s',%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d)
        """%(th.region,0,th.writer_nickname,th.writer_image,th.metapolis,th.title,th.contents,th.contents_image,th.meet_time,
             th.register_time,th.location,th.detail_location,th.location_url,th.total_num)
        self.db.execute(sql)

    # metapolis, title, contents
    # contetents_image, meet_time
    # register_time, location,detail_location
    # location_url, participants_image
    # participants_num, total_num
    def getThunder(self,idx):
        sql = """select * from bd_thunder where thunder_idx = %d"""%(idx)
        row = self.db.executeAll(sql)[0]
        th = Thunder()
        th.setThunder(row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                     row["contents_image"],row["meet_time"],
                     row["register_time"], row["location"],
                     row["detail_location"],row["location_url"],
                     row["participants_image"],row["total_num"])
        th.meet_time = str(th.meet_time)
        th.register_time = str(th.register_time)
        return th

    def getThunderList(self,page):
        sql = """
        select * from bd_thunder order by thunder_idx desc limit %d,%d
        """%((page-1)*15,15)
        rows = self.db.executeAll(sql)
        thunderList = []
        for row in rows:
            th = Thunder()
            th.setThunder(row['region'],row["writer_nickname"],row["writer_image"],row["metapolis"],row["title"],row["contents"],
                         row["contents_image"],row["meet_time"],
                         row["register_time"], row["location"],
                         row["detail_location"],row["location_url"],
                         row["participants_image"],row["total_num"])
            th.meet_time = str(th.meet_time)
            th.register_time = str(th.register_time)
            thunderList.append(th)

        return thunderList
