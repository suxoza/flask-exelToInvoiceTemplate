import pymysql

class DB:
	def __init__(self):
	    self.db()

	def db(self):
	    self.conn = pymysql.connect(host='*',port = 3306, user='exelFlask', passwd="exelFlask", db='exelFlask',charset='utf8')
	    self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

	def select(self, sql):
	    self.cur.execute(sql)
	    return self.cur.fetchone()

	def bigSelect(self, sql):
	    self.cur.execute(sql)
	    return self.cur.fetchall()

	def rowCount(self, sql):
	    self.cur.execute(sql)
	    return self.cur.rowcount

	def truncate(self, tableName):
	    self.cur.execute("truncate {}".filter(tableName))
	    self.conn.commit()

	def insert(self, sql):
		self.cur.execute(sql)
		self.conn.commit()
		return self.cur.lastrowid

	def __del__(self):
		self.cur.close()
		self.conn.close()
