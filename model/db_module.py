import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            host='18.118.131.221',
            id='bappy',
            pw='bappy',
            db_name='bappy'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query,args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, quey, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit():
        self.db.commit()
    def close():
        self.db.close()
