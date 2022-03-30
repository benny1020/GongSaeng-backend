import pymysql
class Database():
    def __init__(self):
        self.db = pymysql.connect(
            #host='18.118.131.221',
            host='127.0.0.1',
            user='benny',
            password='benny',
            db='bappy'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query,args)
        self.db.commit()
        #self.db.close()

    def executeOne(self, query, args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchone()
        #self.db.commit()
        #return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        #self.db.commit()
        return row
    def close(self):
        #self.db.commit()
        self.db.close()
