#encoding:utf-8
import MySQLdb
from MySQLdb import OperationalError
		
def conn(db_name,host='localhost',port=3306,user='root',passwd='root'):
	try:
		conn= MySQLdb.connect(host=host,port = port,user=user,passwd=passwd,db=db_name,)
		return conn.cursor()
	except OperationalError:
		#该数据库不存在
		answer=raw_input('该数据库不存在，是否创建?(yes/no)')
		if answer=='yes' or answer=='':
			conn=MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,)
			cur=conn.cursor()
			cur.execute('create database '+db_name)
			cur.execute('use '+db_name)
			return cur
